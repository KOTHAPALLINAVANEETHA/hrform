# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('Emp_ID', models.CharField(default=1, max_length=10, serialize=False, primary_key=True)),
                ('Name', models.CharField(max_length=30, verbose_name=b'employeename')),
                ('Surname', models.CharField(max_length=30, verbose_name=b'employee_surname')),
                ('ContactNumber', models.CharField(max_length=40)),
                ('emailaddress', models.EmailField(max_length=20, verbose_name=b'email')),
                ('Residentialaddress', models.CharField(max_length=30, verbose_name=b'Residentialaddress')),
                ('EmergencyContact', models.CharField(max_length=40)),
                ('DOB', models.DateField(max_length=10, null=True, blank=True)),
                ('bloodgroup', models.CharField(max_length=10, choices=[(b'O+', b'opositive'), (b'O-', b'Onegative'), (b'AB+', b'ABpositive'), (b'AB-', b'ABnegative')])),
                ('marital_status', models.CharField(max_length=20, choices=[(b'S', b'single'), (b'M', b'married'), (b'U', b'unmarried')])),
                ('Father_name', models.CharField(max_length=30, verbose_name=b'Fathername')),
                ('Mother_name', models.CharField(max_length=40, verbose_name=b'Mothername')),
                ('Spouse_name', models.CharField(max_length=40, verbose_name=b'Spousename')),
                ('kidsdetails', models.IntegerField()),
            ],
        ),
    ]
