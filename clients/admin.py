from django.contrib import admin
from .models import Client
# Register your models here.


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):

    list_display = ["last_name", "first_name", "middle_name", "email"]
    list_filter = ["last_name", "first_name", "middle_name", "email"]
    search_fields = ["last_name", "first_name", "middle_name", "email"]
    ordering = ["last_name", "first_name"]