# -*- coding: utf-8 -*-
from django import forms
from listings.models import Listing


class Form_Listing(forms.ModelForm):
    galary_image = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = Listing
        fields = ['realtor', 'category', 'title',  'address', 'sale_and_rental',  'from_the_sea', 'city', 'state', 'description', 'price', 'bedrooms',
                  'bathrooms', 'garage', 'sqft', 'lot_size', 'vid_name', 'tip_name', 'page_info', 'photo_main',  'is_published',]

        labels = {
            'realtor': 'Риэлторы',
            'title': 'Загаловак',
            'address': 'Адрес',
            'city': 'Город',
            'state': 'Состояние',


        }

        help_texts = {"vid_name": "Вид пример новострой",

                      'tip_name': 'Тип недвижимость',

                      'land_area': 'участка',

                      }


