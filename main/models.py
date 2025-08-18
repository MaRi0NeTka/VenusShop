from django.db import models
from django.utils.text import slugify
''' 
Category - расписываем категорию товара, чтобы понимать, к какой группе он принадлежит

Size - описываем размер товара, используя отдельную модель(для каждого размера)

ProductSize - связываем товар с его размерами и количеством на складе

Product - описываем товар, его характеристики, которые будут отображаться на сайте

ProductImage - описываем дополнительные изображения товара, которые будут отображаться на сайте при заходе на страницу товара
'''

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Size(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
class ProductSize(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='product_sizes')
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.size.name} (in stock {self.stock}) for {self.product.name}'


class Product(models.Model):
    name = models.CharField(max_length=70)
    slug = models.SlugField(max_length=70, unique=True)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    color = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    main_image = models.ImageField(upload_to='product/main/')# лицевое фото товара
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product/extra_photo/')