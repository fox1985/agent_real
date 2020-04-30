# -*- coding: utf-8 -*-
from django import forms
from listings.models import Listing


class Form_Listing(forms.ModelForm):
    galary_image = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = Listing
        fields = ['realtor', 'category', 'title',  'address', 'district', 'region', 'rooms', 'sale_and_rental',  'from_the_sea', 'city', 'state', 'description', 'price', 'bedrooms',
                  'bathrooms', 'garage', 'sqft', 'land_area', 'terrace_area', 'lot_size', 'vid_name', 'tip_name', 'page_info', 'photo_main',  'is_published',]

        labels = {
            'realtor': 'Риэлторы',
            'title': 'Загаловак',
            'address': 'Адрес',
            'city': 'Город',
            'state': 'Состояние',
            'land_area': 'площадь участка',
            'terrace_area': 'площадь террасы',



        }

        help_texts = {"vid_name": "Вид пример новострой",

                      'tip_name': 'Тип недвижимость',

                      'land_area': 'участка',

                      }


class HousesFilterForm(forms.Form):
    """поиск на сайте
    required=False поля не обезательно для запланения
    """
    min_price = forms.DecimalField(label="цена от", required=False, max_digits=10, decimal_places=3,)
    max_price = forms.DecimalField(label="цена до", required=False, max_digits=10, decimal_places=3,)
    rooms = forms.IntegerField(label='Комнат', required=False, )
    bathrooms = forms.IntegerField(label='ванные комнаты', required=False, )
    sale_and_rental = forms.CharField(label='Продажа или аренда', max_length=100,  help_text='Продажа или аренда', required=False, )
    bedrooms = forms.IntegerField(label='спальни', required=False, )
    sqft = forms.IntegerField(label='Квадратные метры', required=False)

                  

    
    