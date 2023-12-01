from django.db import models

# Create your models here.

'''class User(models.Model):
    USER_TYPE_CHOICES = [
        (0, 'Tenant'),
        (1, 'Maintenance'),
        (2, 'Management'),
    ]
    password = models.CharField(max_length=16) 
    user_type = models.IntegerField(choices=USER_TYPE_CHOICES)
'''

class Tenant(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    email = models.CharField(max_length=100)
    unit_number = models.IntegerField()
    date_in = models.DateField()
    date_out = models.DateField(blank=True, null=True)


class MaintenanceRequest(models.Model):
    AREA_CHOICES = [
        (0,'Kitchen'),
        (1, 'Bathroom'),
        (2, 'Living Room'),
        (3, 'Bedroom')
    ]
    area = models.IntegerField(choices = AREA_CHOICES)
    description = models.CharField(max_length=1000)
    image = models.ImageField(blank=True, null=True, upload_to='request_images/')
    status =  models.BooleanField(default=False)
    unit_number = models.IntegerField()
    request_date = models.DateTimeField()
    tenant_key = models.ForeignKey(Tenant, on_delete=models.CASCADE)
