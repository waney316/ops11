from apps.user.models import UserProfile
from rest_framework.authtoken.models import Token
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = "快速生成用户token"

    def handle(self, *args, **options):
        for user in UserProfile.objects.all():
            instance,is_ok = Token.objects.get_or_create(user=user)
            self.stdout.write(self.style.SUCCESS("create userid:{} token {} {}".format(user.id, instance, is_ok)))
