from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


# class User(AbstractUser):
#
#     username = None
#     email = models.EmailField(unique=True, verbose_name="почта")
#     phone_number = models.CharField(max_length=40, verbose_name="телефон")
#
#
#     USERNAME_FIELD = "email"
#     REQUIRED_FIELDS = []
