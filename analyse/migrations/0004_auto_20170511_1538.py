# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-11 15:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('analyse', '0003_auto_20170504_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='uploader',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
