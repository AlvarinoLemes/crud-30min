from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm

def list_products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})