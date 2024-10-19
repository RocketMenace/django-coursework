from django.db import models
from django.urls import reverse
from django.utils import timezone
from clients.models import Client
from users.models import User

# Create your models here.


class Message(models.Model):

    title = models.CharField(max_length=50, verbose_name="тема сообщения")
    body = models.TextField(verbose_name="текст сообщения")

    class Meta:
        verbose_name = "сообщение"
        verbose_name_plural = "сообщения"

    def __str__(self):
        return f"{self.title}"


class NewsLetter(models.Model):

    class Regularity(models.TextChoices):
        DAILY = "ежедневно"
        WEEKLY = "еженедельно"
        MONTHLY = "ежемесячно"

    class Status(models.TextChoices):
        COMPLETED = "завершена"
        CREATED = "создана"
        RUNNING = "запущена"

    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="автор")
    start_date = models.DateTimeField(verbose_name="дата первой отправки")
    end_date = models.DateTimeField(verbose_name="дата завершения")
    message = models.OneToOneField(
        Message,
        on_delete=models.CASCADE,
        related_name="newsletter",
        verbose_name="сообщение",
    )
    recipient = models.ManyToManyField(
        Client, related_name="recipients", verbose_name="получатель"
    )
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.CREATED,
        verbose_name="статус",
    )
    regularity = models.CharField(
        max_length=15, choices=Regularity.choices, verbose_name="периодичность"
    )

    class Meta:
        verbose_name = "рассылка"
        verbose_name_plural = "рассылки"
        ordering = ["status", "start_date"]

    def __str__(self):
        return f"Рассылка: {self.pk}, Статус: {self.status}, Периодичность: {self.regularity}"

    def get_absolute_url(self):
        return reverse("newsletter:detail_newsletter", args=[self.pk])


class DistributionAttempt(models.Model):

    class Status(models.TextChoices):

        SUCCESSFUL = "Успешно"
        UNSUCCESSFUL = "Не успешно"

    last_try = models.DateTimeField(auto_now_add=True, verbose_name="дата отправки")
    status = models.CharField(
        max_length=10, choices=Status.choices, verbose_name="статус"
    )
    server_response = models.TextField(verbose_name="ответ сервера")
    newsletter = models.ForeignKey(
        NewsLetter,
        verbose_name="рассылка",
        on_delete=models.CASCADE,
        related_name="attempts",
    )

    class Meta:

        verbose_name = "попытка рассылки"
        verbose_name_plural = "попытки рассылки"
        ordering = ["-last_try"]

    def __str__(self):
        return f"{self.last_try}-{self.status}"
