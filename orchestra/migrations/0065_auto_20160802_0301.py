# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-02 03:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orchestra', '0064_workercertification_staffbot_enabled'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffingresponse',
            name='request_inquiry',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='responses', to='orchestra.StaffingRequestInquiry'),
        ),
    ]
