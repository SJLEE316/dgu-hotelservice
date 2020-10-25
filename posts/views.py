from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def review(request):
    return render(request, 'posts/review.html')

def reviewadd(request):
    return render(request, 'posts/review_add.html')


def reviewedit(request):
    return render(request, 'posts/review_edit.html')

def create(request):
   if  request.method == "POST":
        chef = request.POST.get('chef')
        menu = request.POST.get('menu')
        content = request.POST.get('content')
        Post.objects.create(chef=chef, menu=menu, content=content)
        return redirect('posts:review')
