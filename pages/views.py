# -*- coding: utf-8 -*-
from django.db.models import Q
from django.shortcuts import render
from listings.forms import HousesFilterForm
from listings.models import Listing, Category


def search_form(request):
    """Поиск на сайте"""
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    categorys = Category.objects.order_by('name').filter(is_published=True)


    'поиск на сайте'
    housesform = HousesFilterForm(request.GET)
    if housesform.is_valid():
        if housesform.cleaned_data['min_price']:
            'Больше или равно'
            listings = listings.filter(price__gte=housesform.cleaned_data['min_price'])

        if housesform.cleaned_data['max_price']:
            'Меньше или равно'
            listings = listings.filter(price__lte=housesform.cleaned_data['max_price'])

        if housesform.cleaned_data['rooms']:
            'Если комнат Больше или равно'
            listings = listings.filter(rooms__gte=housesform.cleaned_data['rooms'])

        if housesform.cleaned_data['rooms']:
            'Если комнат меньше или равно'
            listings = listings.filter(rooms__gte=housesform.cleaned_data['rooms'])

        if housesform.cleaned_data['bathrooms']:
            'ванные комнаты Больше или равно'
            listings = listings.filter(bathrooms__gte=housesform.cleaned_data['bathrooms'])

        if housesform.cleaned_data['bathrooms']:
            'ванные комнаты меньше или равно'
            listings = listings.filter(bathrooms__lte=housesform.cleaned_data['bathrooms'])


        if housesform.cleaned_data['sale_and_rental']:
            'Продажа или аренда Больше или равно'
            listings = listings.filter(sale_and_rental__icontains=housesform.cleaned_data['sale_and_rental'])

        if housesform.cleaned_data['bathrooms']:
            'ванные комнаты меньше или равно'
            listings = listings.filter(bathrooms__lte=housesform.cleaned_data['bathrooms'])


        if housesform.cleaned_data['sale_and_rental']:
            'Продажа или аренда Больше или равно'
            listings = listings.filter(sale_and_rental__icontains=housesform.cleaned_data['sale_and_rental'])

#-----------------------------------------------------------------------------------------------------------------------

        if housesform.cleaned_data['sqft']:
            'Квадратные метры Больше или равно'
            listings = listings.filter(sqft__gte=housesform.cleaned_data['sqft'])

        if housesform.cleaned_data['sqft']:
            'Квадратные метры или аренда меньше или равно'
            listings = listings.filter(sqft__lte=housesform.cleaned_data['sqft'])
#-----------------------------------------------------------------------------------------------------------------------




    context = {'listings': listings, 'categorys': categorys, 'housesform': housesform}
    return render(request, 'listings/listings.html', context)

