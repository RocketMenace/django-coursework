from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from .models import Client
from .forms import ClientCreateForm, ClientUpdateForm
# Create your views here.





class ClientsListView(ListView):

    model = Client
    context_object_name = "clients"

class ClientsDetailView(DetailView):

    model = Client
    context_object_name = "client"

class ClientsCreateView(CreateView):

    template_name = "clients/client_create_form.html"
    model = Client
    context_object_name = "client"
    form_class = ClientCreateForm
    success_url = reverse_lazy("clients:clients")

class ClientsUpdateView(UpdateView):

    template_name = "clients/client_update_form.html"
    model = Client
    context_object_name = "client"
    form_class = ClientUpdateForm
    success_url = reverse_lazy("clients:clients")


class ClientsDeleteView(DeleteView):
    model = Client
    context_object_name = "client"
    success_url = reverse_lazy("clients:clients")
