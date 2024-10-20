from django.db import models
from django.urls import reverse
from users.models import User

# Create your models here.


class Client(models.Model):

    email = models.EmailField(verbose_name="эл.почта")
    last_name = models.CharField(max_length=50, verbose_name="фамилия")
    first_name = models.CharField(max_length=50, verbose_name="имя")
    middle_name = models.CharField(max_length=50, verbose_name="отчество")
    comment = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="владелец")

    class Meta:

        verbose_name = "клиент"
        verbose_name_plural = "клиенты"
        ordering = ["last_name"]
        indexes = [
            models.Index(
                fields=[
                    "last_name",
                ]
            ),
        ]
        permissions = []

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}"

    def get_absolute_url(self):
        return reverse("clients:detail_client", args=[self.pk])

    def get_full_name(self):
        """Returns client's full name."""
        return f"{self.last_name} {self.first_name} {self.middle_name}"
