from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import User
from .forms import UserRegisterForm
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.


class RegisterView(SuccessMessageMixin, CreateView):

    model = User
    context_object_name = "user"
    form_class = UserRegisterForm
    template_name = "users/register.html"
    success_message = "Ссылка для подтверждения направлена на указанный email."
    # success_url = reverse_lazy("newsletter:newsletters")

    def form_valid(self, form):
        user_creation_form = form
        if user_creation_form.is_valid():
            new_user = user_creation_form.save(commit=False)
            new_user.set_password(form.cleaned_data["password"])
            new_user.save()
        return super().form_valid(form)
