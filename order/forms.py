from django import forms
from .models import Order
from listings.models import Listing
from django.forms import Textarea

class OrderForm(forms.ModelForm):
    listing = forms.ModelChoiceField(queryset=Listing.objects.all(), widget=forms.HiddenInput())
    class Meta:
        model = Order
        fields = ['listing', 'name', 'email', 'nomer', 'telephone', 'text']
        widgets = {
            'text': Textarea(attrs={'cols': 25, 'rows': 5}),
        }