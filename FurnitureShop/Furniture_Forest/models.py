from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
# entity
class Product(models.Model) :
    objects = models.Manager()
    name = models.CharField(max_length = 255) # 이름
    price = models.IntegerField() # 가격
    category = models.CharField(max_length = 255, null = True) # 카테고리
    description = models.TextField() # 상품 설명
    thumbnail = models.TextField(null = True) # 상품 이미지 url

class UserManager(BaseUserManager) :
    # 유저 생성
    def _create_user(self, email, username, password, address, **extra_fields) :
        if not email :
            raise ValueError('The given email must be set')

        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(email = email, username = username, address=address, **extra_fields)
        user.set_password(password)
        user.save (using = self._db)
        return user

    # 일반 유저 생성
    def create_user(self, email, username = '', password = None, **extra_fields): 
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, username, password, **extra_fields)

    # 관리자 유저 생성
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff = True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser = True')

        return self._create_user(email, username, password, **extra_fields)

class User(AbstractUser) :
    email = models.EmailField(verbose_name = "email", max_length = 255, unique = True)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    address = models.CharField(max_length=255)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return "<%d %s>" %(self.pk, self.email)
class Basket(models.Model) :
    objects = models.Manager()

    userIdx = models.ForeignKey(User, on_delete=models.CASCADE) # 사용자 idx
    productId = models.ForeignKey(Product, on_delete=models.CASCADE) # 장바구니 안에 담긴 상품의 번호
