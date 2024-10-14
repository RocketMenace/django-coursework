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
def recipients_list(request, pk):
    recipients = NewsLetter.objects.get(pk=pk).recipient.all()
    return render(request, "newsletter/recipients_list.html", {"recipients": recipients})

def main_page(request):
    return render(request, "newsletter/main_page.html")


class NewsLetterListView(ListView):
    model = NewsLetter
    context_object_name = "newsletters"
    queryset = NewsLetter.objects.select_related()



class NewsLetterCreateView(CreateView):

    template_name = "newsletter/newsletter_create_form.html"
    model = NewsLetter
    context_object_name = "newsletter"
    form_class = NewsLetterCreateForm
    success_url = reverse_lazy("newsletter:newsletters")


class NewsLetterDetailView(DetailView):
    model = NewsLetter
    context_object_name = "newsletter"


class NewsLetterUpdateView(UpdateView):
    template_name = "newsletter/newsletter_update_form.html"
    model = NewsLetter
    context_object_name = "newsletter"
    form_class = NewsLetterUpdateForm
    success_url = reverse_lazy("newsletter:newsletters")


class NewsLetterDeleteView(DeleteView):
    model = NewsLetter
    context_object_name = "newsletter"
    success_url = reverse_lazy("newsletter:newsletters")


class MessageListView(ListView):
    model = Message
    context_object_name = "messages"


class MessageCreateView(CreateView):
    model = Message
    form_class = MessageCreateForm
    template_name = "newsletter/message_create_form.html"
    context_object_name = "message"
    success_url = reverse_lazy("newsletter:newsletters")


class MessageDetailView(DetailView):
    model = Message
    context_object_name = "message"


class MessageUpdateView(UpdateView):
    model = Message
    context_object_name = "message"
    form_class = MessageUpdateForm
    template_name = "newsletter/message_update_form.html"
    success_url = reverse_lazy("newsletter:newsletters")


class MessageDeleteView(DeleteView):
    model = Message
    context_object_name = "message"
    success_url = reverse_lazy("newsletter:newsletters")



def distribution_attempts(request, pk):
    attempts = NewsLetter.objects.get(pk=pk).attempts.all()
    return render(request, "newsletter/distributionattempt_list.html", {"attempts": attempts})

