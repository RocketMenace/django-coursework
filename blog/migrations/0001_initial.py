# Generated by Django 4.2 on 2024-10-20 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Article",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100, verbose_name="заголовок")),
                ("body", models.TextField(verbose_name="содержимое")),
                (
                    "image",
                    models.ImageField(
                        upload_to="blog/%Y/%m/%d/", verbose_name="изображение"
                    ),
                ),
                (
                    "views_count",
                    models.PositiveIntegerField(
                        default=0, verbose_name="количество  просмотров"
                    ),
                ),
                (
                    "publish",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="дата публикации"
                    ),
                ),
            ],
            options={
                "verbose_name": "статья",
                "verbose_name_plural": "статьи",
                "ordering": ["-publish"],
            },
        ),
        migrations.AddIndex(
            model_name="article",
            index=models.Index(
                fields=["-publish"], name="blog_articl_publish_2a54df_idx"
            ),
        ),
    ]
