# -*- coding: utf-8 -*-
from django import forms


class HousesFilterForm(forms.Form):
    """поиск на сайте
    required=False поля не обезательно для запланения
    """
    min_price = forms.DecimalField(label="цена от", required=False, max_digits=10, decimal_places=3,)
    max_price = forms.DecimalField(label="цена до", required=False, max_digits=10, decimal_places=3,)
    rooms = forms.IntegerField(label='Комнат', required=False, )
    bathrooms = forms.IntegerField(label='ванные комнаты', required=False,)
    sale_and_rental = forms.CharField(label='Продажа или аренда', max_length=100,  required=False,)
    bedrooms = forms.IntegerField(label='спальни', required=False, )
    sqft = forms.IntegerField(label='Квадратные метры', required=False)