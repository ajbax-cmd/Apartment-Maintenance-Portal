from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home, name = "home"),
    path('tenants/', views.tenants, name = "tenants"),
    path('maintenance_team/', views.maintenance_team, name = "maintenance_team"),
    path('management/', views.management, name = "management"),
    path('update_status/<int:request_id>/', views.update_status, name='update_request_status'),
    path('add_tenant/', views.add_tenant, name = "add_tenant"),
    path('edit_tenant/<int:tenant_id>/', views.edit_tenant, name='edit_tenant'),
    path('delete_tenant/<int:tenant_id>/', views.delete_tenant, name='delete_tenant'),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)