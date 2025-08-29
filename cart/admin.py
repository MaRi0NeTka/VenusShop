from django.contrib import admin

from main.models import ProductSize
from .models import Cart, CartItem


class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 0
    readonly_fields = ('added_at', 'total_price')


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('session_key', 'total_items', 'subtotal')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('session_key',)
    inlines = [CartItemInline] 


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'quantity', 'total_price', 'added_at', 'total_price')
    readonly_fields = ('added_at', 'total_price')
    search_fields = ('cart__session_key', 'product__name')
    list_filter = ('added_at',)
