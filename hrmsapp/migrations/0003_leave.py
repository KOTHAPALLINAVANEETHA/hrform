# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrmsapp', '0002_auto_20170216_1205'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('leaves', models.CharField(max_length=30, choices=[(b'LA', b'leavesavailed'), (b'LAV', b'leavesavailable'), (b'LR', b'leaverequest')])),
            ],
        ),
    ]
