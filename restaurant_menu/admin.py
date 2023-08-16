from django.contrib import admin

from restaurant_menu.models import Item


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("meal", "meal_type", "status", "price",)
    list_filter = ("status",)
    search_fields = ("meal", "price", "meal_type")


admin.site.register(Item, MenuItemAdmin)
