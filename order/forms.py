# -*- coding: utf-8 -*-
from django import forms
from .models import Order
from listings.models import Listing
from django.forms import Textarea
from captcha.fields import CaptchaField

class OrderForm(forms.ModelForm):
    listing = forms.ModelChoiceField(queryset=Listing.objects.all(), widget=forms.HiddenInput())
    captcha = CaptchaField(label='Введите текст с картинки',error_messages={'invalid': 'Неправильный текст'})
    class Meta:
        model = Order
        fields = ['listing', 'name', 'email', 'nomer', 'telephone', 'text', 'captcha']
        widgets = {
            'text': Textarea(attrs={'cols': 25, 'rows': 5}),
        }