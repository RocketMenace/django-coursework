# Generated by Django 4.2 on 2024-10-19 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Client",
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
                ("email", models.EmailField(max_length=254, verbose_name="эл.почта")),
                ("last_name", models.CharField(max_length=50, verbose_name="фамилия")),
                ("first_name", models.CharField(max_length=50, verbose_name="имя")),
                (
                    "middle_name",
                    models.CharField(max_length=50, verbose_name="отчество"),
                ),
                ("comment", models.TextField()),
            ],
            options={
                "verbose_name": "клиент",
                "verbose_name_plural": "клиенты",
                "ordering": ["last_name"],
            },
        ),
        migrations.AddIndex(
            model_name="client",
            index=models.Index(
                fields=["last_name"], name="clients_cli_last_na_392efd_idx"
            ),
        ),
    ]
