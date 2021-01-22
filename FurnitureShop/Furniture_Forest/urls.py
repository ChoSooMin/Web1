from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name="index"),
    path('index.html', views.index),
    path('shop-detail.html', views.shopDetail, name="shopDetail"),
    path('shop.html', views.shop, name="shop"),
    path('shopping-basket.html', views.shoppingBasket, name="shoppingBasket"),
    path('addToBasket', views.addToBasket, name="addToBasket")
]