from django.urls import path, reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from .apps import UsersConfig
from .views import RegisterView
app_name = UsersConfig.name

urlpatterns =[
    path("", LoginView.as_view(template_name="users/login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", RegisterView.as_view(), name="register"),
]