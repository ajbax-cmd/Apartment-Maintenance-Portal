from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect, get_object_or_404
from django import forms
from .models import MaintenanceRequest
from .forms import MaintenanceRequestForm
from django.utils import timezone
from django.db.models import Q
from django.contrib import messages
from .models import Tenant
from .forms import TenantForm
from django.utils.dateparse import parse_date

def home(request):
    return render(request, "home.html")

def tenants(request):
    if request.method == 'POST':
        form = MaintenanceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            # Extract the apartment number from the form
            apartment_number = form.cleaned_data['unit_number']
            tenant_id = form.cleaned_data['tenant_key']

            # Check if the apartment number exists in the Tenant table
            try:
                tenant = Tenant.objects.get(id = tenant_id)
                if(tenant.unit_number != apartment_number):
                    messages.error(request, 'Tenet Key does not match Apartment!.')
                    return render(request, 'tenants.html', {'form': form})

            except Tenant.DoesNotExist:
                # If apartment number does not exist, reject the submission
                messages.error(request, 'Tenet ID does not exist.')
                return render(request, 'tenants.html', {'form': form})

            # If the apartment number exists, proceed with saving the request
            maintenance_request = form.save(commit=False)
            maintenance_request.tenant_key = tenant
            maintenance_request.request_date = timezone.now()  # auto-set the request datetime
            maintenance_request.status = False  # default to False (pending)
            maintenance_request.save()
            messages.success(request, 'Maintenance request submitted successfully.')
            return redirect('home')  # Redirect after successful submission
        else:
            messages.error(request, 'Error submitting request. Please try again.')
    else:
        form = MaintenanceRequestForm()

    return render(request, 'tenants.html', {'form': form})

def maintenance_team(request):
    filters = Q()
    if 'apartment_number' in request.GET:
        apartment_number = request.GET['apartment_number']
        if apartment_number:
            # Directly filter by unit_number since it's an IntegerField
            filters &= Q(unit_number=apartment_number)

    if 'area' in request.GET and request.GET['area']:
        filters &= Q(area=request.GET['area'])

    if 'status' in request.GET and request.GET['status'] != '':
        filters &= Q(status=request.GET['status'] == 'True')  # Convert string to boolean

    # Date range filter (if both dates are provided)
    if 'start_date' in request.GET and 'end_date' in request.GET:
        start_date = request.GET['start_date']
        end_date = request.GET['end_date']
        if start_date and end_date:
            start_date_parsed = parse_date(start_date)
            end_date_parsed = parse_date(end_date)
            if start_date_parsed and end_date_parsed:
                filters &= Q(request_date__date__range=(start_date_parsed, end_date_parsed))

    requests = MaintenanceRequest.objects.filter(filters)
    return render(request, 'maintenance_team.html', {'requests': requests})



def management(request):
    search_query = request.GET.get('search', '')  # Get the search query
    # Filtering tenants based on the search query
    tenants = Tenant.objects.filter(
        Q(id__icontains=search_query) |
        Q(name__icontains=search_query) |
        Q(phone__icontains=search_query) |
        Q(email__icontains=search_query)
    )
    return render(request, 'management.html', {'tenants': tenants, 'search_query': search_query})

def update_status(request, request_id):
    if request.method == 'POST':
        maintenance_request = MaintenanceRequest.objects.get(id=request_id)
        maintenance_request.status = True  # Mark as completed
        maintenance_request.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))  # Redirect back

def add_tenant(request):
    if request.method == 'POST':
        form = TenantForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tenant added successfully.')
            return redirect('management')
    else:
        form = TenantForm()
    return render(request, 'add_tenant.html', {'form': form})

def edit_tenant(request, tenant_id):
    tenant = Tenant.objects.get(id=tenant_id)
    if request.method == 'POST':
        form = TenantForm(request.POST, instance=tenant)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tenant details updated successfully.')
            return redirect('management')
    else:
        form = TenantForm(instance=tenant)
    return render(request, 'edit_tenant.html', {'form': form, 'tenant': tenant})

def delete_tenant(request, tenant_id):
    tenant = Tenant.objects.get(id=tenant_id)
    tenant.delete()
    messages.success(request, 'Tenant deleted successfully.')
    return redirect('management')