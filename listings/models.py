# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from realtors.models import Realtor


class Category(models.Model):
  """Категории"""
  name = models.CharField("Категория", max_length=150)
  is_published = models.BooleanField(default=True, verbose_name=u'Опублековать')

  class Meta:
    db_table = 'category'
    verbose_name = u'Катигории'
    verbose_name_plural = u'Катигория'

  def __unicode__(self):
    return self.name


class Info(models.Model):
  db_table = 'info'
  info_name = models.CharField(max_length=100, verbose_name='Удобства')

  def __unicode__(self):
    return self.info_name

  class Meta:
    verbose_name = u'Удобства'
    verbose_name_plural = u'Удобства'



class Listing(models.Model):
  realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
  title = models.CharField(max_length=200, verbose_name=u'Загаловак')
  category = models.ForeignKey(Category, verbose_name=u"Категория", on_delete=models.SET_NULL, null=True)
  address = models.CharField(max_length=200, verbose_name=u'Адрес')
  city = models.CharField(max_length=100, verbose_name=u'Город')
  state = models.CharField(max_length=100, verbose_name=u'Состояние')
  zipcode = models.CharField(max_length=20, verbose_name=u'почтовый индекс')
  description = models.TextField(blank=True, verbose_name=u'Описание')
  price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=u'цена')
  bedrooms = models.IntegerField(verbose_name=u'спальни')
  bathrooms = models.IntegerField(default=0, verbose_name=u'ванные комнаты')
  garage = models.IntegerField(default=0, verbose_name=u'гараж')
  sqft = models.IntegerField(default=0, verbose_name=u'Квадратные метры')
  lot_size = models.IntegerField(default=0, verbose_name=u'номер ID')
  vid_name = models.CharField(max_length=100, verbose_name=u'вид', help_text=u'Вид недвижимости на пример новострой',blank=True)
  tip_name = models.CharField(max_length=100, verbose_name=u'Тип', help_text=u'Тип недвижимость',blank=True)
  page_info = models.ManyToManyField(Info, verbose_name=u'Удобства',help_text=u'Что есть в доме',blank=True)
  sale_and_rental = models.CharField(max_length=100, verbose_name='Для', help_text='Продажа или аренда',blank=True)
  from_the_sea = models.IntegerField(verbose_name='от моря',default=0, blank=True)
  photo_main = models.ImageField(upload_to='photos-home/%Y/%m/%d/', verbose_name=u'карточтка товара')
  is_published = models.BooleanField(default=True, verbose_name=u'Опублековать')
  list_date = models.DateTimeField(default=datetime.now, blank=True)

  def __unicode__(self):
    return self.title

  class Meta:
    db_table = 'listing'
    verbose_name = u'Объявления'
    verbose_name_plural = u'Объявлени'



class Galary_image(models.Model):
  Listing_page = models.ForeignKey(Listing, blank=True, null=True, on_delete=models.CASCADE)
  galary_image = models.ImageField(upload_to='photos-home/%Y/%m/%d/', verbose_name=u'Картинка', blank=True)

  class Meta:
    db_table = 'galary_image'
    verbose_name = u'Галирея'
    verbose_name_plural = u'Галиреи'