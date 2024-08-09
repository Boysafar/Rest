from django.contrib import admin
from books.models import Product, Sale


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', )


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ('id', 'quantity_sold', 'product')