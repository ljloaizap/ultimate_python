from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

# Create your views here.

# /products --> this is a URL


def index(request):
    # products = Product.objects.filter(score__gte=3)
    # products = Product.objects.get(id=1)
    products = Product.objects.all()

    return render(
        request,
        'index.html',
        context={'products': products}
    )
