from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import (
    CreateView,
    UpdateView,
    ListView,
    DetailView,
    DeleteView,
)
from .forms import (
    NewsLetterCreateForm,
    NewsLetterUpdateForm,
    MessageCreateForm,
    MessageUpdateForm,
)
from .models import NewsLetter, Message, DistributionAttempt


# Create your views here.
@login_required
def recipients_list(request, pk):
    recipients = NewsLetter.objects.get(pk=pk).recipient.all()
    return render(
        request, "newsletter/recipients_list.html", {"recipients": recipients}
    )


@login_required
def main_page(request):
    return render(request, "newsletter/main_page.html")


class NewsLetterListView(LoginRequiredMixin, ListView):
    model = NewsLetter
    context_object_name = "newsletters"
    # queryset = NewsLetter.objects.select_related()

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.select_related("message").filter(author=self.request.user.pk)


class NewsLetterCreateView(LoginRequiredMixin, CreateView):

    template_name = "newsletter/newsletter_create_form.html"
    model = NewsLetter
    context_object_name = "newsletter"
    form_class = NewsLetterCreateForm
    success_url = reverse_lazy("newsletter:newsletters")

    def form_valid(self, form):
        if form.is_valid():
            newsletter = form.save(commit=False)
            newsletter.author = self.request.user.pk
        return super().form_valid(form)


class NewsLetterDetailView(LoginRequiredMixin, DetailView):
    model = NewsLetter
    context_object_name = "newsletter"


class NewsLetterUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "newsletter/newsletter_update_form.html"
    model = NewsLetter
    context_object_name = "newsletter"
    form_class = NewsLetterUpdateForm
    success_url = reverse_lazy("newsletter:newsletters")


class NewsLetterDeleteView(LoginRequiredMixin, DeleteView):
    model = NewsLetter
    context_object_name = "newsletter"
    success_url = reverse_lazy("newsletter:newsletters")


class MessageListView(LoginRequiredMixin, ListView):
    model = Message
    context_object_name = "messages"


class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    form_class = MessageCreateForm
    template_name = "newsletter/message_create_form.html"
    context_object_name = "message"
    success_url = reverse_lazy("newsletter:newsletters")


class MessageDetailView(LoginRequiredMixin, DetailView):
    model = Message
    context_object_name = "message"


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    model = Message
    context_object_name = "message"
    form_class = MessageUpdateForm
    template_name = "newsletter/message_update_form.html"
    success_url = reverse_lazy("newsletter:newsletters")


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    model = Message
    context_object_name = "message"
    success_url = reverse_lazy("newsletter:newsletters")


@login_required
def distribution_attempts(request, pk):
    attempts = NewsLetter.objects.get(pk=pk).attempts.all()
    return render(
        request, "newsletter/distributionattempt_list.html", {"attempts": attempts}
    )
