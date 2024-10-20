from django import forms
from .models import Article


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"

class ArticleCreateForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Article
        fields = ["title", "body", "image"]

class ArticleUpdateForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Article
        fields = ["title", "body", "image"]
