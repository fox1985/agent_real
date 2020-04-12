# -*- coding: utf-8 -*-
"""agent_real URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))

    url(r'^listing/(?P<listing_id>\d+)/$', views.listing, name='listing'),
"""


from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views
from . import  edit

urlpatterns = [
    url(r'^listings/', views.listings, name='listings'),
    url(r'^category/(?P<cat_id>\d+)/$', views.category_page, name='category_page'),#Выборка категорий
    url(r'^listing/(?P<listing_id>\d+)/$', views.listing, name='listing'),

    url(r'^add/$', edit.Form_Galary_View.as_view(), name="new_page"),# Добавить товар


    url(r'^listing/(?P<listing_id>[0-9])/edit/$', edit.Realty_PageUpdate.as_view(), name='edit_page'),# редактировать товар



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)