from django.db import models
from django.contrib.auth.models import AbstractUser,AbstractBaseUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager

# Create your models here.

# class User(AbstractUser):
#     portfolio = models.URLField(blank=True)
#     profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

class CustomUserManager(BaseUserManager):
    def create_user(self,email,password,**extra_fields) :
    #kwargs demedik extra fields dedik
        if not email:
            raise ValueError('Email is mandatory')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)#Kriptolamasi icin böyle yaziyoruz.
        user.save()
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff True.')
        if extra_fields.get('is_active') is not True:
            raise ValueError('Superuser must have is_aktive True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser True.')
        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField('E-Mail Adress', unique=True)
    is_staff = models.BooleanField(default = False)
    is_aktive = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = CustomUserManager()
    
    def __str__(self):
        return self.email