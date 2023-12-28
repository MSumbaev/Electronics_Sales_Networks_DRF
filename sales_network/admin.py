from django.contrib import admin
from django.utils.html import format_html

from sales_network.models import Product, NetworkElement


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'model', 'release_date')
    search_fields = ('title', 'model')


@admin.register(NetworkElement)
class NetworkElementAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    list_display = ('id', 'title', 'element_type', 'email', 'country', 'city', 'supplier_link', 'debt',)
    list_display_links = ('id', 'title',)
    filter_horizontal = ('products',)
    list_filter = ('element_type', 'country', 'city',)
    search_fields = ('title', 'email')
    actions = ('clear_out_the_debt',)

    def supplier_link(self, obj):
        supplier = NetworkElement.objects.get(id=obj.supplier_id)

        return format_html("<a href='{url}'>{description}</a>", description=f"{supplier}",
                           url=f"/admin/sales_network/networkelement/{supplier.id}")

    @admin.action(description="Очистить задолженность")
    def clear_out_the_debt(self, request, queryset):
        queryset.update(debt=0)
