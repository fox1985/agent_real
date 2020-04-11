# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from order.models import Order

# Register your models here.
@admin.register(Order)
class AdmeinOrder(admin.ModelAdmin):
    list_display = ('listing', 'name', 'email', 'nomer', 'text' )
    ordering = ['listing',]