# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrmsapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Official',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Designations', models.CharField(max_length=40, choices=[(b'ACC', b'Accountant'), (b'TL', b'Teamlead'), (b'Exe', b'executive'), (b'Man', b'manager'), (b'LA', b'linuxadministrator'), (b'NT', b'networktrainer'), (b'PD', b'pythondeveloper'), (b'TM', b'traineemanager'), (b'US-IT', b'us-it recruiter'), (b'TC', b'technicalconsultant'), (b'SR', b'seniorexecutive'), (b'ASST', b'assistantmanager'), (b'MD', b'microsoftdynamics-practicehead'), (b'SA', b'systemadministrator'), (b'INT', b'intern'), (b'LI', b'linuxintern'), (b'OA', b'officeassistant')])),
                ('DOJ', models.DateField(max_length=20, null=True, blank=True)),
                ('Supervisor', models.CharField(max_length=40, verbose_name=b'supervisor')),
                ('Subordinates', models.CharField(max_length=20, verbose_name=b'subordinates')),
                ('departments', models.CharField(max_length=20, choices=[(b'ES', b'ES01'), (b'ES', b'ES02'), (b'ES', b'ES03'), (b'ES', b'ES04'), (b'ES', b'ES05'), (b'ES', b'ES06'), (b'ES', b'ES07'), (b'ES', b'ES08'), (b'ES', b'ES09'), (b'ES', b'ES10'), (b'ES', b'ES12'), (b'ES', b'ES13')])),
            ],
        ),
        migrations.AlterField(
            model_name='personal',
            name='kidsdetails',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='official',
            name='EMP_ID',
            field=models.ForeignKey(to='hrmsapp.Personal'),
        ),
    ]
