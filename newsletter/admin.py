from django.contrib import admin
from .models import Message, DistributionAttempt, NewsLetter
# Register your models here.

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ["title", "body"]
    list_filter = ["title"]
    search_fields = ["title"]


@admin.register(DistributionAttempt)
class DistributionAttempt(admin.ModelAdmin):
    list_display = ["last_try", "status"]
    list_filter = ["status" , "last_try"]
    search_fields = ["status", "last_try"]
    ordering = ["status", "-last_try"]


@admin.register(NewsLetter)
class NewsLetterAdmin(admin.ModelAdmin):
    list_display = ["start_date", "status", "regularity"]
    list_filter = ["start_date", "status", "regularity"]
    search_fields = ["status", "regularity"]
    ordering = ["status", "start_date"]
