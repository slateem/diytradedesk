# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-19 13:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('diy_dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trade',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
