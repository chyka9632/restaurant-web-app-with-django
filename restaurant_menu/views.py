from django.shortcuts import render
from django.views import generic

from restaurant_menu.models import Item


class MenuList(generic.ListView):    # Class-based view
    queryset = Item.objects.order_by("date_created")
    template_name = "index.html"
    pass


class MenuItemDetails(generic.DetailView):
    model = Item
    template_name = "menu_item_detail.html"
    pass


