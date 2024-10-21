from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):

        group = Group(name="контент менеджер")
        group.save()
        users_ct = ContentType.objects.get_for_model(User)
        can_view_newsletters = Permission.objects.get(codename="Can_view_newsletters")

        can_edit_newsletters = Permission.objects.get(codename="Can_edit_newsletter")
        can_view_users = Permission(
            name="can view", codename="Can_view_users", content_type=users_ct
        )
        can_change_users = Permission(
            name="can change", codename="Can_change_user_status", content_type=users_ct
        )
        Permission.objects.bulk_create(
            [
                can_change_users,
                can_view_users,
            ]
        )
        group.permissions.set(
            [
                can_view_newsletters,
                can_change_users,
                can_view_users,
                can_edit_newsletters,
            ]
        )
