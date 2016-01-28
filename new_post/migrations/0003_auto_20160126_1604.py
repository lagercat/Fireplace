# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-26 16:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('new_post', '0002_auto_20160126_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='submitter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
