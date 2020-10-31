from django.urls import path
from .views import *

app_name="posts"   
urlpatterns=[

    path('review', review, name="review"),
    path('reviewadd', review_add, name="review_add"),
    path('reviewedit/<int:id>/', review_edit, name="review_edit"),
    path('create/', create, name="create"),
    path('delete/<int:id>/', delete, name="delete"),
]