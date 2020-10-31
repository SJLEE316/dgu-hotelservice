from django.shortcuts import render
from .models import *

# Create your views here.
def productList(request):
    products = Product.objects.all()
    return render(request, 'products/productList.html', {'products':products})

def cart(request):
    return render(request, 'products/cart.html')

def order(request):
    return render(request, 'products/order.html')

def thankyou(request):
    return render(request, 'products/thankyou.html')
