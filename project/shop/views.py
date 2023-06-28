from django.shortcuts import render
from rest_framework import viewsets

from shop.models import Product, Review
from shop.serializers import ProductSerializer, PureReviewSerializer

from shop.tasks import send_to_admin
from django.core.mail import send_mail, mail_admins

# Create your views here.


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = PureReviewSerializer

    def create(self, request, *args, **kwargs):
        result = super().create(request, *args, **kwargs)

        send_to_admin.delay('hey', 'hey1')

        return result
