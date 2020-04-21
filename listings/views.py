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
from django.views.generic.list import ListView
from django.db.models import Q

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



class SearchListView(ListView):
    model = Listing
    template_name = 'pages/index.html'
    context_object_name = 'listings'

    def get_queryset(self):
      # Получаем не отфильтрованный кверисет всех моделей
      queryset = Listing.objects.all()
      q = self.request.GET.get("q")
      if q:
        # Если 'q' в GET запросе, фильтруем кверисет по данным из 'q'
        return queryset.filter(Q(bathrooms=q), Q(rooms=q))
      return queryset