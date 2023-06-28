from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=1000)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    short_description = models.CharField(max_length=1000)
    description = models.CharField(max_length=10000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
    
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='reviews')
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=10000)
    rate = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.user.username}: {self.product.name}"
    
class ProductSpecification(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='specification')
    specification = models.ForeignKey(
        Specification, on_delete=models.CASCADE)
    value = models.CharField(max_length=1000)

    def __str__(self) -> str:
        return f"{self.product.name}: {self.specification.name}"
