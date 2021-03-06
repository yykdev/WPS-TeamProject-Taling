# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-23 11:14
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('regiclass', '0002_auto_20170822_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrollment',
            name='class_day',
            field=models.CharField(blank=True, max_length=8),
        ),
        migrations.AlterField(
            model_name='enrollment',
            name='class_time',
            field=models.CharField(blank=True, max_length=24),
        ),
        migrations.AlterField(
            model_name='enrollment',
            name='location',
            field=models.CharField(blank=True, max_length=24),
        ),
        migrations.AlterField(
            model_name='enrollment',
            name='to_tutor',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='enrollment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tutor_info', to=settings.AUTH_USER_MODEL),
        ),
    ]
