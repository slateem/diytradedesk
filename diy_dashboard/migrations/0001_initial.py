# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-18 13:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(blank=True, max_length=20, verbose_name='Symbol')),
                ('entry_date', models.DateField(verbose_name='Entry Date')),
                ('strategy', models.CharField(blank=True, max_length=50, verbose_name='Strategy')),
                ('quantity', models.IntegerField(default=1, verbose_name='Quantity')),
                ('entry_price', models.FloatField(blank=True, default=0, null=True, verbose_name='Entry Price')),
                ('risk', models.FloatField(blank=True, default=0, null=True, verbose_name='Risk')),
                ('target', models.FloatField(blank=True, default=0, null=True, verbose_name='Target')),
                ('exit_price', models.FloatField(blank=True, default=0, null=True, verbose_name='Exit Price')),
                ('exit_date', models.DateField(blank=True, null=True, verbose_name='Exit Date')),
                ('exit_reason', models.TextField(blank=True, null=True, verbose_name='Exit Reason')),
                ('profit_loss', models.FloatField(blank=True, default=0, null=True, verbose_name='Profit/Loss')),
                ('percent_change', models.FloatField(blank=True, default=0, null=True, verbose_name='Percent Change')),
            ],
        ),
    ]