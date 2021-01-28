from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Product, User, Basket
from django.contrib import auth, messages

# baseUrl/
def index(request) :
    return render(request, 'Furniture_Forest/index.html')

# baseUrl/shop
def shop(request, category) :
    # 목록을 가져오고, 리스트에 저장
    if category == "all":
        productList = Product.objects.all()
    else:
        productList = Product.objects.filter(category=category)

    context = { "productList": productList, "category": category } # 데이터 저장 객체
    
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
    product_quantity = int(request.POST['product_quantity'])

    product = Product.objects.get(pk=product_id) 
    context = { "product": product }

    if request.user.is_authenticated:
        curUser = request.user

        basket = Basket.objects.filter(userIdx=curUser, productId=product).first()

        if basket is not None:
            quantity = basket.productQuantity
            basket.productQuantity = quantity + product_quantity
            basket.save()

            messages.info(request, '장바구니에 추가되었습니다.')
        else:
            insertBasket = Basket(userIdx=curUser, productId=product, productQuantity=product_quantity)
            insertBasket.save()

            messages.info(request, '장바구니에 추가되었습니다.')
    else :
        messages.info(request, '로그인되어있지 않습니다.')

    return render(request, 'Furniture_Forest/shop-detail.html', context)

# baseUrl/shopping-basket.html
def shoppingBasket(request) :
    if request.user.is_authenticated: # 로그인 O
        basketList = Basket.objects.filter(userIdx = request.user)
        productList = []

        for basket in basketList:
            product = basket.productId
            productList.append(product)
            
        context = { "productList": productList } # 데이터 저장 객체

        return render(request, 'Furniture_Forest/shopping-basket.html', context)
    else: # 로그인 X
        messages.info(request, '로그인되어있지 않습니다.')
        return HttpResponseRedirect(reverse('login'))

    return render(request, 'Furniture_Forest/shopping-basket.html')

def deleteItem(request) :
    curProduct = request.POST['curProduct']
    curUser = request.user
    basketItem = Basket.objects.filter(userIdx=curUser, productId=curProduct).first()
    basketItem.delete()

    return HttpResponseRedirect(reverse('shoppingBasket'))

def deleteAllBasket(request) :
    basketItems = Basket.objects.all()
    basketItems.delete()

    return HttpResponseRedirect(reverse('shoppingBasket'))

# 로그인
def login(request) :
    # POST 방식의 request가 들어오면, 로그인을 해주고
    if request.method == "POST":
        email = request.POST['email']
        pw = request.POST['pw']

        user = auth.authenticate(request, email=email, password=pw)

        if user is not None:
            auth.login(request, user) # 로그인하고
            return HttpResponseRedirect(reverse('index')) # index 페이지로 이동
        else:
            messages.error(request, '이메일 또는 비밀번호가 올바르지 않습니다')
            return render(request, 'Furniture_Forest/login.html')
    
    else:
        # 아니라면 로그인 화면을 렌더링한다.
        return render(request, 'Furniture_Forest/login.html')

# 로그아웃
def logOut(request) :
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))

# 회원가입
def signUp(request) :
    # POST 방식의 request가 들어오면, 회원가입을 해주고
    if request.method == "POST":
        # 회원가입 후, 로그인 화면으로 이동
        email = request.POST['email']
        pw = request.POST['password']
        name = request.POST['name']
        address = request.POST['address']
        
        try :
            user = User.objects.create_user(email=email, username=name, password=pw, address=address)
        except Exception as ex: # DB Error
            messages.error(request, '이미 존재하는 회원 정보입니다')
            return render(request, 'Furniture_Forest/sign-up.html')

        # 정상적으로 회원가입이 되었다면
        auth.login(request, user) # 로그인하고
        return HttpResponseRedirect(reverse('index')) # 인덱스 페이지로 이동

    # 아니라면 회원가입 화면을 렌더링해준다.
    return render(request, 'Furniture_Forest/sign-up.html')