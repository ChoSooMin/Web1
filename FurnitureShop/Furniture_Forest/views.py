from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Product, User
from django.contrib import auth

# baseUrl/
def index(request) :
    return render(request, 'Furniture_Forest/index.html')

# baseUrl/shop
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

# 로그인
def login(request) :
    # POST 방식의 request가 들어오면, 로그인을 해주고
    if request.method == "POST":
        email = request.POST['email']
        pw = request.POST['pw']

        user = auth.authenticate(request, email=email, password=pw)

        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'Furniture_Forest/login.html', {'error': '이메일 또는 비밀번호가 올바르지 않습니다'})
    
    else:
        # 아니라면 로그인 화면을 렌더링한다.
        return render(request, 'Furniture_Forest/login.html')

# 회원가입
def signUp(request) :
    # POST 방식의 request가 들어오면, 회원가입을 해주고
    if request.method == "POST":
        # 회원가입 후, 로그인 화면으로 이동
        email = request.POST['email']
        pw = request.POST['password']
        name = request.POST['name']
        address = request.POST['address']
        
        user = User.objects.create_user(email=email, username=name, password=pw, address=address)
        # auth.login(request, user)
        return HttpResponseRedirect(reverse('index'))

    # 아니라면 화면을 렌더링해준다.
    return render(request, 'Furniture_Forest/sign-up.html')