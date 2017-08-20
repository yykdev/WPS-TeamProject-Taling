# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-19 15:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0003_remove_tutor_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank=True, unique=True),
        ),
    ]