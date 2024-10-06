from django import forms
from django.forms import DateTimeField, DateTimeInput, SplitDateTimeWidget

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


class MessageCreateForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Message
        fields = "__all__"


class MessageUpdateForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Message
        fields = "__all__"
