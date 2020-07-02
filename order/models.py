# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime
from  listings.models import Listing

from django.db import models
from django.utils.translation import ugettext_lazy as _



# Create your models here.
class Order(models.Model):
    listing = models.ForeignKey(Listing, verbose_name='список')
    name = models.CharField(max_length=100, verbose_name='Имя')
    email = models.EmailField()
    nomer = models.CharField(max_length=100, verbose_name='Номер ID')
    telephone = models.CharField(max_length=100, verbose_name='Телефон')
    text = models.TextField(verbose_name='Сообщения',)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)


    class Meta:
        verbose_name = u'Заявка'
        verbose_name_plural = u'Заявки'
