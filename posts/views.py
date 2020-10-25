from django.shortcuts import render

# Create your views here.
def review(request):
    return render(request, 'posts/review.html')

def reviewadd(request):
    return render(request, 'posts/review_add.html')


def reviewedit(request):
    return render(request, 'posts/review_edit.html')
