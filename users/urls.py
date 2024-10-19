from django.urls import path, reverse_lazy
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordChangeDoneView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)
from .apps import UsersConfig
from .views import RegisterView, VerificationView


app_name = UsersConfig.name

urlpatterns = [
    # Login / Logout usrl
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    # Change password urls
    path("password-change/", PasswordChangeView.as_view(), name="password_change"),
    path(
        "password-change/done/",
        PasswordChangeDoneView.as_view(),
        name="password_change_done",
    ),
    # Reset password urls
    path("password-reset", PasswordResetView.as_view(), name="password_reset"),
    path(
        "password-reset/done",
        PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "password-reset/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "password-reset/complete/",
        PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
    # User register url.
    path("", RegisterView.as_view(), name="register"),
    path("activate/<uid64>/<token>", VerificationView.as_view(), name="verification"),
]
