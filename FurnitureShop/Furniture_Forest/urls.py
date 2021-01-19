from django.urls import path
from . import views

urlpatterns=[
    path('', views.index),
    path('index.html', views.index),
    path('shop-single.html', views.shopSingle),
    path('shop.html', views.shop),
    path('shopping-basket.html', views.shoppingBasket)
]