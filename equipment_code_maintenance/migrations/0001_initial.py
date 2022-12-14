# Generated by Django 4.0.6 on 2022-07-18 14:03

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EquipmentCodeMaintenance',
            fields=[
                ('EquipmentCodeID', models.AutoField(primary_key=True, serialize=False)),
                ('ECDescription', models.CharField(max_length=100, verbose_name='Equipment Code Class')),
                ('ECBillingCode', models.CharField(max_length=20, verbose_name='Billing Codes')),
                ('ECDefaultRates', models.IntegerField(blank=True, default=16, null=True, verbose_name='Default Hourly Rates')),
                ('ECActive', models.CharField(choices=[('Y', 'Active'), ('N', 'Inactive')], default='Y', max_length=1)),
                ('LastUpdatedBy', models.IntegerField(blank=True, null=True)),
                ('ECDateAdded', models.DateField(auto_now_add=True, verbose_name='Date Added')),
                ('ECDateUpdated', models.DateField(auto_now=True, verbose_name='Date Updated')),
                ('ECDateActivated', models.DateField(null=True, verbose_name='Date Activated')),
            ],
            managers=[
                ('dj_equipment_code', django.db.models.manager.Manager()),
            ],
        ),
    ]
