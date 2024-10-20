from django import forms
from .models import Client


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"


class ClientCreateForm(StyleFormMixin, forms.ModelForm):

    class Meta:

        model = Client
        fields = "__all__"
        exclude = [
            "owner",
        ]


class ClientUpdateForm(StyleFormMixin, forms.ModelForm):

    class Meta:

        model = Client
        fields = "__all__"
        exclude = [
            "owner",
        ]


class ClientDeleteForm(StyleFormMixin, forms.Form):

    class Meta:
        model = Client
