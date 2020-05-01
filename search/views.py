# -*- coding: utf-8 -*-
from django.db.models import Q
from django.shortcuts import render
from search.forms import HousesFilterForm
from listings.models import Listing, Category


def search_form(request):
    """Поиск на сайте"""
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    categorys = Category.objects.order_by('name').filter(is_published=True)


    'поиск на сайте'
    housesform = HousesFilterForm(request.GET)
    if housesform.is_valid():
        if housesform.cleaned_data['min_price']:
            'Меньше или равно'
            listings = listings.filter(price__gte=housesform.cleaned_data['min_price'])

        if housesform.cleaned_data['max_price']:
            'Больше или равно'
            listings = listings.filter(price__lte=housesform.cleaned_data['max_price'])


#-----------------------------------------------------------------------------------------------------------------------

        if housesform.cleaned_data['sqft']:
            'Квадратные метры Больше или равно'
            listings = listings.filter(sqft__gte=housesform.cleaned_data['sqft'])

        if housesform.cleaned_data['sqft']:
            'Квадратные метры или аренда меньше или равно'
            listings = listings.filter(sqft__lte=housesform.cleaned_data['sqft'])
#-----------------------------------------------------------------------------------------------------------------------

        if housesform.cleaned_data['bedrooms']:
            'спальни больше или равно'
            listings = listings.filter(bedrooms__gte=housesform.cleaned_data['bedrooms'])



        if housesform.cleaned_data['bedrooms']:
            'спальни менше или равно'
            listings = listings.filter(bedrooms__lte=housesform.cleaned_data['bedrooms'])
#---------------------------------------------------------------------------------------------------------------------

        if housesform.cleaned_data['city']:
            'Город'
            listings = listings.filter(city__icontains=housesform.cleaned_data['city'])

#---------------------------------------------------------------------------------------------------------------------

        if housesform.cleaned_data['title']:
            'Вид недвижимости'
            listings = listings.filter(title__icontains=housesform.cleaned_data['title'])



    context = {'listings': listings, 'categorys': categorys, 'housesform': housesform}
    return render(request, 'listings/listings.html', context)

