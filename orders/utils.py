import secrets
import string
import datetime
from .models import Coupon # Assuming you have a coupon
from DailyOperatingHours import DailyOperatingHours

def generate_coupon_code(length=10):
    """
    Generate a unique alphanumeric coupon code.
    """
    characters=string.ascii_letters+string.digits
    while True:
        code=''.join(secrets.choice(characters) for _ in range(length))
        if not Coupon.objects.filter(code=code).exists():
            return code

def get_today_operating_hours():
    today=datetime.date.today().strftime('%A')
    try:
        hours=DailyOperatingHours.objects.get(day=today)
        return (hours.open_time,hours.close_time)
    except DailyOperatingHours.DoesNotExist:
        return (None,None)

