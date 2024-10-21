from django import forms
from django.forms import DateTimeInput
from django.utils import timezone

from clients.models import Client
from .models import NewsLetter, Message


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"


class NewsLetterCreateForm(StyleFormMixin, forms.ModelForm):

    def __init__(self, *args, **kwargs):

        self.request = kwargs.pop("request")
        super(NewsLetterCreateForm, self).__init__(*args, **kwargs)
        self.fields["recipient"].queryset = Client.objects.filter(
            owner=self.request.user
        )
        self.fields["message"].queryset = Message.objects.filter(
            owner=self.request.user
        )

    class Meta:
        model = NewsLetter
        fields = "__all__"
        exclude = [
            "owner",
        ]
        widgets = {
            "start_date": DateTimeInput(
                format="%Y-%m-%d %H:%M", attrs={"type": "datetime-local"}
            ),
            "end_date": DateTimeInput(
                format="%Y-%m-%d %H:%M", attrs={"type": "datetime-local"}
            ),
        }

    def clean_start_date(self):
        cd = self.cleaned_data
        if cd["start_date"] < timezone.now():
            raise forms.ValidationError("Нельзя указать прошедшее время.")
        return cd["start_date"]

    def clean_end_date(self):
        cd = self.cleaned_data
        if cd["end_date"] < timezone.now():
            raise forms.ValidationError("Нельзя указать прошедшее время.")
        return cd["end_date"]


class NewsLetterUpdateForm(StyleFormMixin, forms.ModelForm):

    def __init__(self, *args, **kwargs):

        self.request = kwargs.pop("request")
        super(NewsLetterUpdateForm, self).__init__(*args, **kwargs)
        self.fields["recipient"].queryset = Client.objects.filter(
            owner=self.request.user
        )
        self.fields["message"].queryset = Message.objects.filter(
            owner=self.request.user
        )

    class Meta:
        model = NewsLetter
        fields = "__all__"
        exclude = [
            "owner",
        ]
        widgets = {
            "start_date": DateTimeInput(
                format="%Y-%m-%d %H:%M", attrs={"type": "datetime-local"}
            ),
            "end_date": DateTimeInput(
                format="%Y-%m-%d %H:%M", attrs={"type": "datetime-local"}
            ),
        }

    def clean_start_date(self):
        cd = self.cleaned_data
        if cd["start_date"] < timezone.now():
            raise forms.ValidationError("Нельзя указать прошедшее время.")
        return cd["start_date"]

    def clean_end_date(self):
        cd = self.cleaned_data
        if cd["end_date"] < timezone.now():
            raise forms.ValidationError("Нельзя указать прошедшее время.")
        return cd["end_date"]


class MessageCreateForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Message
        fields = "__all__"
        exclude = [
            "owner",
        ]


class MessageUpdateForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Message
        fields = "__all__"
        exclude = [
            "owner",
        ]


class ContentManagerUpdateNewsLetterForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = NewsLetter
        fields = [
            "status",
        ]
