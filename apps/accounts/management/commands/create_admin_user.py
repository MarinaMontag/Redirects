from django.contrib.auth import get_user_model
from django.core.management import BaseCommand


class Command(BaseCommand):
    ADMIN_USERNAME = 'admin@mail.com'
    ADMIN_PASSWORD = 'adminpassword'  # nosec  # noqa: S105
    help = 'Check and create default development admin user'

    def handle(self, *args, **options):
        user_class = get_user_model()

        user, _ = user_class.objects.update_or_create(
            username=self.ADMIN_USERNAME,
            defaults={
                'is_superuser': True,
                'is_staff': True,
            },
        )
        user.set_password(self.ADMIN_PASSWORD)
        user.save()
        self.stdout.write(self.style.SUCCESS('Development admin user has been created!'))
