from django.db import models

# Create your models here.
# entity
class Product(models.Model) :
    objects = models.Manager()
    name = models.CharField(max_length = 255) # 이름
    price = models.IntegerField() # 가격
    category = models.CharField(max_length = 255, null = True) # 카테고리
    description = models.TextField() # 상품 설명
    thumbnail = models.TextField(null = True) # 상품 이미지 url

class User(models.Model) :
    objects = models.Manager()

    email = models.EmailField()
    pw = models.CharField(max_length = 255)
    name = models.CharField(max_length = 255)
    address = models.CharField(max_length = 255, null = True)
class Basket(models.Model) :
    objects = models.Manager()

    userIdx = models.ForeignKey(User, on_delete=models.CASCADE) # 사용자 idx
    productId = models.ForeignKey(Product, on_delete=models.CASCADE) # 장바구니 안에 담긴 상품의 번호
