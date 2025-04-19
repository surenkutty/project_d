from django.core.management.base import BaseCommand
from django.utils import timezone
from dindigul.models import Offers

class Command(BaseCommand):
    help = 'Deactivate all expired offers.'

    def handle(self, *args, **kwargs):
        now = timezone.now()
        expired_offers = Offers.objects.filter(is_active=True, end_date__lt=now)
        count = expired_offers.update(is_active=False)
        self.stdout.write(self.style.SUCCESS(f'{count} expired offers deactivated.'))
