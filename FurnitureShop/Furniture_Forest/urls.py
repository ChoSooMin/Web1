from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name="index"),
    path('shopDetail/', views.shopDetail, name="shopDetail"),
    path('shoppingBasket/', views.shoppingBasket, name="shoppingBasket"),
    path('shoppingBasket/addToBasket/', views.addToBasket, name="addToBasket"),
    path('shoppingBasket/deleteItem/', views.deleteItem, name="deleteItem"),
    path('shoppingBasket/deleteAllBasket/', views.deleteAllBasket, name="deleteAllBasket"),
    path('login/', views.login, name="login"),
    path('logOut/', views.logOut, name="logOut"),
    path('signUp/', views.signUp, name="signUp"),
    path('shop/', views.shop, name="shop"),
    path('shop/<str:category>/', views.shop, name="shopCategory")
]