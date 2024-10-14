from django import forms
from django.forms import DateTimeField, DateTimeInput, SplitDateTimeWidget
from django.utils import timezone
from .models import NewsLetter, Message, DistributionAttempt


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"


class NewsLetterCreateForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = NewsLetter
        fields = "__all__"
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

    class Meta:
        model = NewsLetter
        fields = "__all__"
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


class MessageUpdateForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Message
        fields = "__all__"
