# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Trade(models.Model):
	user = models.ForeignKey(User)
	symbol = models.CharField("Symbol", max_length=20, blank=True)
	entry_date = models.DateField("Entry Date")
	strategy = models.CharField("Strategy", max_length=50, blank=True)
	quantity = models.IntegerField("Quantity", default=1)
	entry_price = models.FloatField("Entry Price", blank=True, null=True, default=0)
	risk = models.FloatField("Risk", blank=True, null=True, default=0)
	target = models.FloatField("Target", blank=True, null=True, default=0)
	exit_price = models.FloatField("Exit Price", blank=True, null=True, default=0)
	exit_date = models.DateField("Exit Date", blank=True, null=True)
	exit_reason = models.TextField("Exit Reason", blank=True, null=True)
	profit_loss = models.FloatField("Profit/Loss", blank=True, null=True, default=0)
	percent_change = models.FloatField("Percent Change", blank=True, null=True, default=0)
