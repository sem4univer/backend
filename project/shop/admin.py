from django.contrib import admin

# Register your models here.
from shop.models import Product, Review, ProductSpecification

admin.site.register(Product)
admin.site.register(Review)
