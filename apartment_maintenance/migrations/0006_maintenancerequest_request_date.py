# Generated by Django 2.1.5 on 2023-11-30 09:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('apartment_maintenance', '0005_auto_20231130_0221'),
    ]

    operations = [
        migrations.AddField(
            model_name='maintenancerequest',
            name='request_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]