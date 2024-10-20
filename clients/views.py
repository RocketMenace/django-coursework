from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DetailView,
    DeleteView,
)

from clients.custom_mixins import (
    ClientOwnerCreateMixin,
    ClientOwnerUpdateMixin,
    ClientOwnerMixin,
)
from .forms import ClientCreateForm, ClientUpdateForm
from .models import Client


# Create your views here.


class ClientsListView(ClientOwnerMixin, ListView):

    context_object_name = "clients"
    permission_required = "clients.Can_view_clients"

class ClientsDetailView(DetailView):

    model = Client
    context_object_name = "client"
    permission_required = "clients.Can_edit_clients"


class ClientsCreateView(ClientOwnerCreateMixin, CreateView):

    context_object_name = "client"
    form_class = ClientCreateForm
    permission_required = "clients.Can_create_clients"


class ClientsUpdateView(ClientOwnerUpdateMixin, UpdateView):

    context_object_name = "client"
    form_class = ClientUpdateForm
    permission_required = "clients.Can_edit_clients"


class ClientsDeleteView(ClientOwnerMixin, DeleteView):
    context_object_name = "client"
    permission_required = "clients.Can_delete_clients"

