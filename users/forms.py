from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"


class UserRegisterForm(StyleFormMixin, UserCreationForm):

    class Meta:
        model = User
        fields = ["email", "password1", "password2"]

    def clean_email(self):
        data = self.cleaned_data["email"]
        if User.objects.only("email").filter(email=data).exists():
            raise forms.ValidationError("Пользователь с таким email уже существует.")
        return data
