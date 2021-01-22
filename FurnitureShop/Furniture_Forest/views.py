from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Product

# baseUrl/ or baseUrl/index.html
def index(request) :
    return render(request, 'Furniture_Forest/index.html')

# baseUrl/shop.html
def shop(request) :
    # 목록을 가져오고, 리스트에 저장
    productList = Product.objects.all()
    context = { "productList": productList } # 데이터 저장 객체
    
    return render(request, 'Furniture_Forest/shop.html', context)

# baseUrl/shop-detail.html
def shopDetail(request) : 
    # query에서 product_id를 가져온다.
    product_id = request.GET['product_id'] # queryStr으로 보내는 건 GET
    product = Product.objects.get(pk=product_id)
    context = { "product": product }

    return render(request, 'Furniture_Forest/shop-detail.html', context)

# baseUrl/addToBasket
def addToBasket(request) :
    product_id = request.POST['product_id']
    product_quantity = request.POST['product_quantity']
    # print(product_id)
    # print(product_quantity)
    product = Product.objects.get(pk=product_id)
    context = { "product": product }
    # alert 창 띄워서 "계속 쇼핑하시겠습니까?" 예 : shop-detail.html 아니오 : shopping-basket.html
    return render(request, 'Furniture_Forest/shop-detail.html', context)

# baseUrl/shopping-basket.html
def shoppingBasket(request) :
    return render(request, 'Furniture_Forest/shopping-basket.html')

def login(request) :
    return render(request, 'Furniture_Forest/login.html')