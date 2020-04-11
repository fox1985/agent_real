# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime
from  listings.models import Listing

from django.db import models


# Create your models here.
class Order(models.Model):
    listing = models.ForeignKey(Listing, verbose_name='список')
    name = models.CharField(max_length=100, verbose_name='Имя',)
    email = models.EmailField()
    date = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        verbose_name = u'Форма обртной связи'
        verbose_name_plural = u'Форма обртной связи'
