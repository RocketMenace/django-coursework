from django.db import models
from django.utils import timezone
# Create your models here.

class Article(models.Model):

    title = models.CharField(max_length=100, verbose_name="заголовок")
    body = models.TextField(verbose_name="содержимое")
    image = models.ImageField(upload_to="blog/", verbose_name="изображение")
    views_count = models.PositiveIntegerField(default=0, verbose_name="количество  просмотров")
    publish = models.DateTimeField(auto_now_add=timezone.now(), verbose_name="дата публикации")

    class Meta:

        verbose_name = "статья"
        verbose_name_plural = "статьи"
        ordering = ["-publish"]
        indexes = [models.Index(fields=["-publish"]),]

    def __str__(self):
        return f"{self.title}"

