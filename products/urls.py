from django.urls import path
from .views import *

app_name="products"
urlpatterns=[
    path('productList', productList, name="productList"),
]