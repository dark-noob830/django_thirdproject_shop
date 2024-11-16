from celery import shared_task
from zoneinfo import ZoneInfo

from accounts.models import OtpCode
from datetime import datetime, timedelta


@shared_task
def remove_expired_otp_codes():
    expire_time = datetime.now(tz=ZoneInfo('Asia/Tehran')) - timedelta(minutes=2)
    OtpCode.objects.filter(created_at__lt=expire_time).delete()
