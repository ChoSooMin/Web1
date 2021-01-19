from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request) :
    return render(request, 'Furniture_Forest/index.html')

def shopSingle(request) : 
    return render(request, 'Furniture_Forest/shop-single.html')

def shop(request) :
    return render(request, 'Furniture_Forest/shop.html')

def shoppingBasket(request) :
    return render(request, 'Furniture_Forest/shopping-basket.html')