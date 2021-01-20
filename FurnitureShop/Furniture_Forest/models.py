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