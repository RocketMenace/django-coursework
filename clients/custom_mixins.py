from newsletter.custom_mixins import OwnerEditMixin, OwnerMixin
from clients.models import Client
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class ClientOwnerMixin(
    OwnerMixin, OwnerEditMixin, LoginRequiredMixin, PermissionRequiredMixin
):

    model = Client
    success_url = reverse_lazy("clients:clients")


class ClientOwnerCreateMixin(ClientOwnerMixin):

    template_name = "clients/client_create_form.html"


class ClientOwnerUpdateMixin(ClientOwnerMixin):

    template_name = "clients/client_update_form.html"
