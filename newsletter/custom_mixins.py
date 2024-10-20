from django.core.exceptions import PermissionDenied

from .models import NewsLetter
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from .models import NewsLetter, Message


class OwnerMixin:

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.is_staff:
            return qs.select_related().all()
        return qs.select_related().filter(owner=self.request.user.pk)


class OwnerEditMixin:

    def form_valid(self, form):
        form.instance.owner = self.request.user

        return super().form_valid(form)




class NewsLetterOwnerMixin(OwnerMixin, LoginRequiredMixin, PermissionRequiredMixin):

    model = NewsLetter
    success_url = reverse_lazy("newsletter:newsletters")
    permission_denied_message = "Для совершения этого действия обратитесь к администратору"


class NewsLetterOwnerCreateMixin(NewsLetterOwnerMixin, OwnerEditMixin):

    template_name = "newsletter/newsletter_create_form.html"


class NewsLetterOwnerUpdateMixin(NewsLetterOwnerMixin, OwnerEditMixin):

    template_name = "newsletter/newsletter_update_form.html"


class MessageOwnerMixin(OwnerMixin, PermissionRequiredMixin, LoginRequiredMixin):

    model = Message
    success_url = reverse_lazy("newsletter:newsletters")

class MessageOwnerCreateMixin(MessageOwnerMixin, OwnerEditMixin):

    template_name = "newsletter/message_create_form.html"

class MessageOwnerUpdateMixin(MessageOwnerMixin, OwnerEditMixin):

    template_name = "newsletter/message_update_form.html"

