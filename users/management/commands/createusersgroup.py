from pyexpat.errors import messages

from IPython.core.compilerop import code_name
from django.contrib.auth.models import Group, Permission
from django.core.management import BaseCommand
from django.contrib.contenttypes.models import ContentType
from newsletter.models import NewsLetter, Message
from clients.models import Client


class Command(BaseCommand):

    def handle(self, *args, **options):
        group = Group(name="Пользователи платформы")
        group.save()
        newsletter_ct = ContentType.objects.get_for_model(NewsLetter)
        message_ct = ContentType.objects.get_for_model(Message)
        clients_ct = ContentType.objects.get_for_model(Client)
        can_view_newsletters = Permission(
            name="Can view",
            codename="Can_view_newsletters",
            content_type=newsletter_ct,
        )
        can_edit_newsletters = Permission(
            name="Can change",
            codename="Can_edit_newsletter",
            content_type=newsletter_ct,
        )
        can_create_newsletters = Permission(
            name="Can create",
            codename="Can_create_newsletter",
            content_type=newsletter_ct,
        )
        can_delete_newsletters = Permission(
            name="Can delete",
            codename="Can_delete_newsletter",
            content_type=newsletter_ct,
        )
        can_view_messages = Permission(
            name="Can view", codename="Can_view_message", content_type=message_ct
        )
        can_edit_messages = Permission(
            name="Can edit", codename="Can_edit_message", content_type=message_ct
        )
        can_create_messages = Permission(
            name="Can create", codename="Can_create_message", content_type=message_ct
        )
        can_delete_messages = Permission(
            name="Can delete", codename="Can_delete_message", content_type=message_ct
        )
        can_view_clients = Permission(
            name="Can view", codename="Can_view_clients", content_type=clients_ct
        )
        can_edit_clients = Permission(
            name="Can edit", codename="Can_edit_clients", content_type=clients_ct
        )
        can_create_clients = Permission(
            name="Can create", codename="Can_create_clients", content_type=clients_ct
        )
        can_delete_clients = Permission(
            name="Can delete", codename="Can_delete_clients", content_type=clients_ct
        )
        Permission.objects.bulk_create(
            [
                can_view_newsletters,
                can_edit_newsletters,
                can_create_newsletters,
                can_delete_newsletters,
                can_view_messages,
                can_edit_messages,
                can_create_messages,
                can_delete_messages,
                can_view_clients,
                can_edit_clients,
                can_create_clients,
                can_delete_clients,

            ]
        )
        group.permissions.set(
            [
                can_view_newsletters,
                can_edit_newsletters,
                can_create_newsletters,
                can_delete_newsletters,
                can_view_messages,
                can_edit_messages,
                can_create_messages,
                can_delete_messages,
                can_view_clients,
                can_edit_clients,
                can_create_clients,
                can_delete_clients,
            ]
        )
