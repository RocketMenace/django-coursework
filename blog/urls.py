from django.urls import path
from django.views.decorators.cache import cache_page

from .views import (
    ArticleCreateView,
    ArticleDeleteView,
    ArticleDetailView,
    ArticleUpdateView,
    main_page
)
from .apps import BlogConfig

app_name = BlogConfig.name

urlpatterns = [
    path("", cache_page(10)(main_page), name="main_page"),
    # path("", ArticleListView.as_view(), name="main_page"),
    path("create/", ArticleCreateView.as_view(), name="create_article"),
    path("detail/<int:pk>/", ArticleDetailView.as_view(), name="detail_article"),
    path("update/<int:pk>/", ArticleUpdateView.as_view(), name="update_article"),
    path("delete/<int:pk>", ArticleDeleteView.as_view(), name="delete_article"),
]
