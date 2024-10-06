from django.urls import path
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
    main_page, DistributionAttemptListView, recipients_list
)
from .apps import NewsletterConfig

app_name = NewsletterConfig.name

urlpatterns = [
    path("", main_page, name="main_page"),
    path(
        "create_newsletter/", NewsLetterCreateView.as_view(), name="create_newsletter"
    ),
    path(
        "detail_newsletter/<int:pk>",
        NewsLetterDetailView.as_view(),
        name="detail_newsletter",
    ),
    path("newsletters/", NewsLetterListView.as_view(), name="newsletters"),
    path(
        "edit_newsletter/<int:pk>",
        NewsLetterUpdateView.as_view(),
        name="edit_newsletter",
    ),
    path(
        "delete_newsletter/<int:pk>", NewsLetterDeleteView.as_view(), name="delete_newsletter"
    ),
    path("create_message/", MessageCreateView.as_view(), name="create_message"),
    path("detail_message/<int:pk>", MessageDetailView.as_view(), name="detail_message"),
    path("edit_message/<int:pk>", MessageUpdateView.as_view(), name="edit_message"),
    path("delete_message/<int:pk>", MessageDeleteView.as_view(), name="delete_message"),
    path("attempts/", DistributionAttemptListView.as_view(), name="attempts"),
    path("recipients/<int:pk>", recipients_list, name="recipients")
]
