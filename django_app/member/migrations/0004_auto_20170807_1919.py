# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-07 10:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0003_auto_20170807_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutor',
            name='cert_type',
            field=models.CharField(choices=[('univ', '대학인증'), ('grad', '대학원인증'), ('identity', '신분증인증')], max_length=1),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='status_type',
            field=models.CharField(choices=[('ing', '재학'), ('graduation', '졸업'), ('complete', '수료')], max_length=1, null=True),
        ),
    ]
