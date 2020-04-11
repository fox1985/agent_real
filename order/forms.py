from django import forms
from .models import Order
from listings.models import Listing

class OrderForm(forms.ModelForm):
    listing = forms.ModelChoiceField(queryset=Listing.objects.all(), widget=forms.HiddenInput())
    class Meta:
        model = Order
        fields = ['listing', 'name', 'email',]