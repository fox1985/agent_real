# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

# Register your models here.
from .models import Listing, Info, Galary_image, Category

class CategoryAdmin(TranslationAdmin):
  list_display = ('name', 'is_published', )
  list_editable = ('is_published',)

class Galary_image_Admin(admin.TabularInline):
  model = Galary_image
  extra = 4

class InfoAdmin(TranslationAdmin):
  list_display = ('info_name',)

class ListingAdmin(TranslationAdmin):
  inlines = [Galary_image_Admin]
  list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor', 'floors')
  list_display_links = ('id', 'title')
  list_filter = ('realtor',)
  list_editable = ('is_published',)
  search_fields = ('title', 'description', 'address', 'city', 'state',  'price', )
  list_per_page = 25





admin.site.register(Listing, ListingAdmin)
admin.site.register(Info,InfoAdmin)
admin.site.register(Category, CategoryAdmin)