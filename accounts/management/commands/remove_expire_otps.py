from zoneinfo import ZoneInfo

from django.core.management.base import BaseCommand, CommandError
from accounts.models import OtpCode
from datetime import datetime, timedelta


class Command(BaseCommand):
    help = 'Remove all expired OTP code'
    def handle(self, *args, **options):
        expire_time = datetime.now(tz=ZoneInfo('Asia/Tehran')) - timedelta(minutes=2)
        OtpCode.objects.filter(created_at__lt=expire_time).delete()
        self.stdout.write('all expired OTP code removed')
