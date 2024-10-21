from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="электронная почта")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:

        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"
        indexes = [
            models.Index(fields=["email"]),
        ]
        permissions = [
            ("change_user_is_active", "Can change user status"),
        ]
