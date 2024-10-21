from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    UpdateView,
    ListView,
    DetailView,
    DeleteView,
)

from .custom_mixins import (
    NewsLetterOwnerMixin,
    NewsLetterOwnerCreateMixin,
    NewsLetterOwnerUpdateMixin,
    MessageOwnerCreateMixin,
    MessageOwnerUpdateMixin,
    MessageOwnerMixin,
)
from .forms import (
    NewsLetterCreateForm,
    NewsLetterUpdateForm,
    MessageCreateForm,
    MessageUpdateForm,
    ContentManagerUpdateNewsLetterForm,
)
from .models import NewsLetter, Message


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


class NewsLetterListView(NewsLetterOwnerMixin, ListView):
    context_object_name = "newsletters"
    permission_required = "newsletter.Can_view_newsletters"


class NewsLetterCreateView(NewsLetterOwnerCreateMixin, CreateView):

    context_object_name = "newsletter"
    form_class = NewsLetterCreateForm
    permission_required = "newsletter.Can_create_newsletter"

    def get_form_kwargs(self):

        kwargs = super(NewsLetterCreateView, self).get_form_kwargs()
        kwargs["request"] = self.request
        return kwargs


class NewsLetterDetailView(DetailView):
    model = NewsLetter
    context_object_name = "newsletter"
    permission_required = "newsletter.Can_edit_newsletter"


class NewsLetterUpdateView(NewsLetterOwnerUpdateMixin, UpdateView):
    context_object_name = "newsletter"
    form_class = NewsLetterUpdateForm
    permission_required = "newsletter.Can_edit_newsletter"

    def get_form_class(self):
        if self.request.user.is_staff:
            return ContentManagerUpdateNewsLetterForm
        return NewsLetterUpdateForm

    def get_form_kwargs(self):

        kwargs = super(NewsLetterUpdateView, self).get_form_kwargs()
        kwargs["request"] = self.request
        return kwargs

class NewsLetterDeleteView(NewsLetterOwnerMixin, DeleteView):

    context_object_name = "newsletter"
    permission_required = "newsletter.Can_delete_newsletter"


class MessageListView(MessageOwnerMixin, ListView):
    context_object_name = "messages"
    permission_required = "newsletter.Can_view_message"


class MessageCreateView(MessageOwnerCreateMixin, CreateView):
    form_class = MessageCreateForm
    context_object_name = "message"
    permission_required = "newsletter.Can_create_message"


class MessageDetailView(DetailView):
    model = Message
    context_object_name = "message"
    permission_required = "newsletter.Can_edit_message"


class MessageUpdateView(MessageOwnerUpdateMixin, UpdateView):
    context_object_name = "message"
    form_class = MessageUpdateForm
    permission_required = "newsletter.Can_edit_message"


class MessageDeleteView(MessageOwnerMixin, DeleteView):
    context_object_name = "message"
    permission_required = "newsletter.Can_delete_message"


@login_required
def distribution_attempts(request, pk):
    attempts = NewsLetter.objects.get(pk=pk).attempts.all()
    return render(
        request, "newsletter/distributionattempt_list.html", {"attempts": attempts}
    )
