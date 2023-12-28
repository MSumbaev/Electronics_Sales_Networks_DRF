from django.contrib import admin

from sales_network.models import Product, NetworkElement


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'model', 'release_date')
    search_fields = ('title', 'model')


@admin.register(NetworkElement)
class NetworkElementAdmin(admin.ModelAdmin):
    list_display = ('title', 'element_type', 'email', 'country', 'city', 'supplier', 'debt',)
    list_filter = ('element_type', 'country', 'city',)
    search_fields = ('title', 'email')
