# -*- coding: utf-8 -*-
from django import forms


class HousesFilterForm(forms.Form):
    """поиск на сайте
    required=False поля не обезательно для запланения
    """
    min_price = forms.DecimalField(label="цена от", required=False, max_digits=10, decimal_places=3,)
    max_price = forms.DecimalField(label="цена до", required=False, max_digits=10, decimal_places=3,)
    rooms = forms.IntegerField(label='Комнат', required=False, )
    bathrooms = forms.IntegerField(label='Санузел', required=False,)
    bedrooms = forms.IntegerField(label='спальни', required=False, )
    sqft = forms.IntegerField(label='Квадратные метры', required=False)
    city = forms.CharField(label='Город', required=False,)
    vid_name = forms.CharField(label='Вид недвижимости', required=False)