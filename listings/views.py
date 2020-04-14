# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from listings.models import Listing, Category, Galary_image
from django.contrib import auth
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .choices import price_choices, bedroom_choices, state_choices
from order.forms import OrderForm
from django.core.urlresolvers import reverse

# Create your views here.


def listings(request, page_nober=1):
    """Главная страныица listings"""
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    categorys = Category.objects.order_by('name').filter(is_published=True)

    paginator = Paginator(listings, 6)  # выводит сколько страници  должно быть до погинации


    context = {'listings': paginator.page(page_nober), 'categorys': categorys}
    return render(request, 'listings/listings.html', context)


def category_page(request, cat_id):
  """Выборка категорий
    1 создать словарь
    2 выбрать отну страницу из категории#филтрует категорию выбирает категорию
    3 выводить из базы через словарь имя категории
    4 фильтровать страницу и категории
    5 выводить страницы через словарь
  """
  context_dict = {}
  try:

    category = Category.objects.get(pk=cat_id)  # выбрать одну категорию
    context_dict['category_name'] = category.name  # Вытошеть имя категории

    listings = Listing.objects.filter(category=category).prefetch_related('galary_image_set').all()

    context_dict['listings'] = listings  # для вывода страницы

    context_dict['galary_image'] = Galary_image.objects.filter(pk=cat_id)  # Филтует галирею изображений



    categorys = Category.objects.order_by('name').filter(is_published=True)

    context_dict['categorys'] = categorys # для вывода меню на в файле category.html

    context_dict['username'] = auth.get_user(request).username  # Афторизация пользователя


  except Category.DoesNotExist:
    pass

  return render(request, 'listings/category.html', context_dict)


def listing(request, listing_id):
  """Страница listing"""
  listing = get_object_or_404(Listing, pk=listing_id)
  categorys = Category.objects.order_by('name').filter(is_published=True)
  form = OrderForm(request.POST or None, initial={'listing': listing} )

  if request.method == "POST":
    if form.is_valid():
      form.save()
      send_mail('Заявка от torrehome.ru', 'Зайдите в админку чтобы почетать заявку http://torrehome.ru/admin/ ',  'http://torrehome.ru/admin/',
                ['artemdav2@gmail.com'], fail_silently=False)
      return  HttpResponseRedirect("{}?sended=True".format(reverse('listing', kwargs={'listing_id': listing_id})), )




  context = {
    'listing': listing,
    'categorys': categorys,
    'form' : form,
    'sended': request.GET.get("sended", False)
  }

  return render(request, 'listings/listing.html', context)




def search(request):
  "Посик"
  queryset_list = Listing.objects.order_by('-list_date')

  # Keywords
  if 'keywords' in request.GET:
    keywords = request.GET['keywords']
    if keywords:
      queryset_list = queryset_list.filter(description__icontains=keywords)

  # City
  if 'city' in request.GET:
    city = request.GET['city']
    if city:
      queryset_list = queryset_list.filter(city__iexact=city)

  # State
  if 'state' in request.GET:
    state = request.GET['state']
    if state:
      queryset_list = queryset_list.filter(state__iexact=state)

  # Bedrooms
  if 'bedrooms' in request.GET:
    bedrooms = request.GET['bedrooms']
    if bedrooms:
      queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

  # Price
  if 'price' in request.GET:
    price = request.GET['price']
    if price:
      queryset_list = queryset_list.filter(price__lte=price)

  context = {
    'state_choices': state_choices,
    'bedroom_choices': bedroom_choices,
    'price_choices': price_choices,
    'listings': queryset_list,
    'values': request.GET
  }

  return render(request, 'listings/search.html', context)