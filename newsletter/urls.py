from django.urls import path
from django.views.decorators.cache import cache_page

from .models import DistributionAttempt
from .views import (
    NewsLetterListView,
    NewsLetterCreateView,
    NewsLetterDeleteView,
    NewsLetterDetailView,
    NewsLetterUpdateView,
    MessageListView,
    MessageCreateView,
    MessageUpdateView,
    MessageDetailView,
    MessageDeleteView,
    main_page, recipients_list, distribution_attempts
)
from .apps import NewsletterConfig

app_name = NewsletterConfig.name

urlpatterns = [

    path("", main_page, name="main_page"),

    # CRUD urls for newsletter.
    path(
        "create_newsletter/", NewsLetterCreateView.as_view(), name="create_newsletter"
    ),
    path(
        "detail_newsletter/<int:pk>",
        NewsLetterDetailView.as_view(),
        name="detail_newsletter",
    ),
    path("newsletters/", cache_page(60)(NewsLetterListView.as_view()), name="newsletters"),
    path(
        "edit_newsletter/<int:pk>",
        NewsLetterUpdateView.as_view(),
        name="edit_newsletter",
    ),
    path(
        "delete_newsletter/<int:pk>", NewsLetterDeleteView.as_view(), name="delete_newsletter"
    ),

    #CRUD urls for messages.
    path("create_message/", MessageCreateView.as_view(), name="create_message"),
    path("detail_message/<int:pk>", MessageDetailView.as_view(), name="detail_message"),
    path("edit_message/<int:pk>", MessageUpdateView.as_view(), name="edit_message"),
    path("delete_message/<int:pk>", MessageDeleteView.as_view(), name="delete_message"),


    # url for getting recipients list.
    path("recipients/<int:pk>", recipients_list, name="recipients"),

    # url for
    path("newsletters/<int:pk>/attempts/", distribution_attempts, name="attempts"),
]
