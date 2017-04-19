# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Trade
from .forms import TradeForm

@login_required
def index(request):
	trades = Trade.objects.filter(user=request.user)
	return render(request, 'diy_dashboard/index.html', {
		'trades': trades,
		'user': request.user,
	})

@login_required
def trade_create(request):
	form = TradeForm()
	if request.method == 'POST':
		form = TradeForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('dashboard')
	return render(request, 'diy_dashboard/trade/create.html', {
		'form': form,
	})

@login_required
def trade_edit(request, pk):
	trade = Trade.objects.get(pk=pk)
	trade.entry_date = trade.entry_date.strftime('%m/%d/%Y')
	trade.exit_date = trade.exit_date.strftime('%m/%d/%Y')
	form = TradeForm(instance=trade)
	if request.method == 'POST':
		form = TradeForm(request.POST, instance=trade)
		if form.is_valid():
			form.save()
			return redirect('dashboard')
	return render(request, 'diy_dashboard/trade/edit.html', {
		'form': form,
	})

@login_required
def trade_detail(request, pk):
	pass

@login_required
def trade_delete(request, pk):
	Trade.objects.filter(pk=pk).delete()
	return redirect('dashboard')
