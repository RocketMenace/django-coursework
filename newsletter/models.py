from django.db import models

# Create your models here.


class Message(models.Model):

    title = models.CharField(max_length="50", verbose_name="тема сообщения")
    body = models.TextField()

    class Meta:
        verbose_name = "сообщение"
        verbose_name_plural = "сообщения"

    def __str__(self):
        return f"{self.title}"


class DistributionAttempt(models.Model):

    class Status(models.TextChoices):

        SUCCESSFUL = "Успешно"
        UNSUCCESSFUL = "Не успешно"

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="дата отправки")
    status = models.CharField(max_length=10, choices=Status.choices, verbose_name="статус")
    server_response = models.TextField(verbose_name="ответ сервера")


    class Meta:

        verbose_name = "попытка рассылки"
        verbose_name_plural = "попытки рассылки"

    def __str__(self):
        return f"{self.created_at}-{self.status}"




class NewsLetter(models.Model):

    pass
