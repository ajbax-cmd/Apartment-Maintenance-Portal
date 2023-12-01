from django import forms
from .models import MaintenanceRequest
from django.contrib import messages
from .models import Tenant

class MaintenanceRequestForm(forms.ModelForm):
    tenant_key = forms.IntegerField(label='Tenant ID', required=True)
    class Meta:
        model = MaintenanceRequest
        fields = ['unit_number', 'area', 'description', 'image']
        widgets = {
            'unit_number': forms.NumberInput(attrs={'required': True}),
            'area': forms.RadioSelect(choices=MaintenanceRequest.AREA_CHOICES),
            'description': forms.Textarea(attrs={'required': True}),
            'image': forms.FileInput(),
        }

class TenantForm(forms.ModelForm):
    class Meta:
        model = Tenant
        fields = ['name', 'phone', 'email', 'unit_number', 'date_in', 'date_out']