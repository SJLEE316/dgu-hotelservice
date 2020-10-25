from django.urls import path
from .views import *

app_name="pages"
urlpatterns=[
     path('cart', cart, name="cart"),
     path('order', order, name="order"),
     path('thankyou', thankyou, name="thankyou"),
     path('review', review, name="review"),
     path('reviewadd', reviewadd, name="reviewadd"),
     path('reviewedit', reviewedit, name="reviewedit"),
     path('create/', create, name="create"),

]