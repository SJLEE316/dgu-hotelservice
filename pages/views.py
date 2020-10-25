from django.shortcuts import render, redirect, get_object_or_404
from .models import *

# Create your views here.

def cart(request):
    return render(request, 'pages/cart.html')

def order(request):
    return render(request, 'pages/order.html')

def thankyou(request):
    return render(request, 'pages/thankyou.html')

def review(request):
    return render(request, 'pages/review.html')

def reviewadd(request):
    return render(request, 'pages/review_add.html')


def reviewedit(request):
    return render(request, 'pages/review_edit.html')

def new(request):
    return render(request, 'pages/review_add.html')

def create(request):
    if request.method == "POST":
        chef=request.POST.get('chef')
        menu=request.POST.get('menu')
        content=request.POST.get('content')
        image=request.FILES.get('image')
        Post.objects.create(content=content,menu=menu,chef=chef, image=image)
        return redirect('pages:review')  
