from django.urls import path
from .views import *

app_name="products"
urlpatterns=[
    path('productList', productList, name="productList"),
    path('cart', cart, name="cart"),
    path('order', order, name="order"),
    path('thankyou', thankyou, name="thankyou"),

]