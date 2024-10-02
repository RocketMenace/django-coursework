from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from .models import Client
# Create your views here.


def base_view(request):
    return render(request, "clients/base.html")


class ClientsListView(ListView):

    model = Client
    context_object_name = "clients"

class ClientsDetailView(DetailView):
    model = Client
    context_object_name = "client"

class ClientsCreateView(CreateView):
    model = Client
    context_object_name = "client"
    # form_class = ClientCreateForm

class ClientsUpdateView(UpdateView):
    model = Client
    context_object_name = "client"

class ClientsDeleteView(DeleteView):
    model = Client
    context_object_name = "client"
