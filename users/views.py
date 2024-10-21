from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views import View
from django.views.generic import CreateView, ListView, DetailView, UpdateView

from config.settings import EMAIL_HOST_USER
from .forms import UserRegisterForm, UserUpdateForm
from .models import User
from .token_generator import verification_token
from django.contrib.auth.models import Group

# Create your views here.


class RegisterView(SuccessMessageMixin, CreateView):

    model = User
    context_object_name = "user"
    form_class = UserRegisterForm
    template_name = "users/register.html"
    success_message = "Ссылка для подтверждения направлена на указанный email."
    success_url = "#"

    def form_valid(self, form):
        user_creation_form = form
        if user_creation_form.is_valid():
            new_user = user_creation_form.save(commit=False)
            new_user.set_password(form.cleaned_data["password1"])
            new_user.is_active = False
            new_user.save()
            domain = get_current_site(self.request).domain
            uid64 = urlsafe_base64_encode(force_bytes(new_user.pk))
            token = verification_token.make_token(new_user)
            link = reverse(
                "users:verification", kwargs={"uid64": uid64, "token": token}
            )
            activate_url = "http://" + domain + link
            email = user_creation_form.cleaned_data["email"]
            subject = "Уведомление о регистрации на платформе"
            message = f"Для завершения регистрации перейдите по ссылке {activate_url}"
            send_mail(
                subject,
                message,
                EMAIL_HOST_USER,
                [
                    email,
                ],
                fail_silently=True,
            )
        return super().form_valid(form)


class VerificationView(View):

    def get(self, request, uid64, token):
        uid64 = force_str(urlsafe_base64_decode(uid64))
        user = User.objects.get(pk=uid64)
        user.is_active = True
        group = Group.objects.get(name="Пользователи платформы")
        user.groups.add(group)
        user.save()
        return redirect("users:login")


class UsersListView(ListView):
    model = User
    context_object_name = "users"

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(is_staff=False)


class UsersDetailView(UpdateView):
    model = User
    context_object_name = "user"
    form_class = UserUpdateForm
    success_url = reverse_lazy("users:users_list")

    def form_valid(self, form):
        if self.request.method == "POST":
            form.save()
        else:
            form = form
        return super().form_valid(form)
