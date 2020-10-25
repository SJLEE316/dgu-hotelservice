from django.urls import path
from .views import *

app_name="posts"   
urlpatterns=[

    path('review', review, name="review"),
    path('reviewadd', reviewadd, name="reviewadd"),
    path('reviewedit', reviewedit, name="reviewedit"),
    path('create/', create, name="create"),
]