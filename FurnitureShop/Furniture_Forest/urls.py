from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name="index"),
    path('shopDetail/', views.shopDetail, name="shopDetail"),
    path('shop/', views.shop, name="shop"),
    path('shoppingBasket/', views.shoppingBasket, name="shoppingBasket"),
    path('addToBasket', views.addToBasket, name="addToBasket"),
    path('login/', views.login, name="login"),
    path('signUp/', views.signUp, name="signUp")
]