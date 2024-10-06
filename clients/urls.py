from config.urls import path
from clients.apps import ClientsConfig
from .views import (
    ClientsListView,
    ClientsDetailView,
    ClientsCreateView,
    ClientsDeleteView,
    ClientsUpdateView,
)


app_name = ClientsConfig.name

urlpatterns = [
    path("", ClientsListView.as_view(), name="clients"),
    path("create_client/", ClientsCreateView.as_view(), name="create_client"),
    path("delete_client/<int:pk>", ClientsDeleteView.as_view(), name="delete_client"),
    path("edit_client/<int:pk>", ClientsUpdateView.as_view(), name="edit_client"),
    path("detail_client/<int:pk>", ClientsDetailView.as_view(), name="detail_client"),
]
