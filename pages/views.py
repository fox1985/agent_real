# -*- coding: utf-8 -*-
from django.db.models import Q
from django.views.generic import TemplateView, ListView

from listings.models import Listing


class HomePageView(TemplateView):
    template_name = 'listings/listings.html'


class SearchResultsView(ListView):
    model = Listing
    template_name = 'pages/search_results.html'
    context_object_name = 'listings'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Listing.objects.filter(
            Q(bathrooms__contains=query) | Q(rooms__icontains=query)
        )
        return object_list