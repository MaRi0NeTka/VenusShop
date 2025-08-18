from django.contrib import admin
from .models import Category, Size, \
    ProductSize, Product, ProductImage

class ProductSizeInline(admin.TabularInline):
    model = ProductSize
    extra = 1

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1 # Количество дополнительных полей для изображений продукта, ячейка для загрузки фото/выбора размера и т.д.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')
    list_filter = ('category',)
    search_fields = ('name', 'category__name')
    prepopulated_fields = {'slug': ('name',)} # автоматическая транслитерация для поля slug из поля name
    inlines = [ProductSizeInline, ProductImageInline]

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}  # автоматическая транслитерация для поля slug из поля name

class SizeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Size, SizeAdmin)
admin.site.register(Product, ProductAdmin)