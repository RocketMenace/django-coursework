from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import User
from .forms import UserRegisterForm
# Create your views here.


class RegisterView(CreateView):

    model = User
    context_object_name = "user"
    form_class = UserRegisterForm
    template_name = "users/register.html"
    success_url = reverse_lazy("newsletter:newsletters")