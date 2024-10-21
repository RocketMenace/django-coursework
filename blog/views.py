from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    UpdateView,
    DetailView,
    DeleteView,
)

from newsletter.models import NewsLetter
from .forms import ArticleCreateForm, ArticleUpdateForm
from .models import Article


# Create your views here.


#


class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleCreateForm
    success_url = reverse_lazy("blog:main_page")


class ArticleDetailView(DetailView):
    model = Article
    context_object_name = "article"

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class ArticleUpdateView(UpdateView):
    model = Article
    form_class = ArticleUpdateForm
    success_url = reverse_lazy("blog:main_page")


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy("blog:main_page")


def main_page(request):
    newsletters_count = NewsLetter.objects.count()
    newsletters_count_active = NewsLetter.objects.filter(status="запущена").count()
    newsletter_unique_clients = (
        NewsLetter.objects.prefetch_related("recipients").distinct().count()
    )
    articles = Article.objects.order_by("?")[:3]
    context = {
        "newsletters_count": newsletters_count,
        "newsletters_count_active": newsletters_count_active,
        "newsletter_unique_clients": newsletter_unique_clients,
        "articles": articles,
    }
    return render(request, "blog/blog_main_page.html", context)
