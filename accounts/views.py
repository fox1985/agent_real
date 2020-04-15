# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from order.models import Order

def login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username, password=password)

    if user is not None:
      auth.login(request, user)
      messages.success(request, 'Вы вошли в систему')
      return redirect('listings')
    else:
      messages.error(request, 'Неверные учетные данные')
      return redirect('login')
  else:
    return render(request, 'accounts/login.html')



def logout(request):
  if request.method == 'POST':
    auth.logout(request)
    messages.success(request, 'Вы вышли из системы')
    return redirect('index')


