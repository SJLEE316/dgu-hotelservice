from django.shortcuts import render

# Create your views here.

def cart(request):
    return render(request, 'pages/cart.html')

def order(request):
    return render(request, 'pages/order.html')

def thankyou(request):
    return render(request, 'pages/thankyou.html')

def review(request):
    return render(request, 'pages/review.html')