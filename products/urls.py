from django.urls import path
from .views import *

app_name="products"
urlpatterns=[
    path('productlist', product_list, name="product_list"),
    path('cart', cart, name="cart"),
    path('order', order, name="order"),
    path('thankyou', thankyou, name="thankyou"),

]