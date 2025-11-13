import secrets
import string
import datetime
from .models import Coupon # Assuming you have a coupon
from DailyOperatingHours import DailyOperatingHours

def generate_coupon_code(length=10):
    """Generate a unique alphanumeric coupon code."""
    if not isinstance(length,int)or length<=0:
        return ValueError("Length must be a positive integer")
    characters=string.ascii_uppercase+string.ascii_lowercase+string.digits
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

def calculate_tip_amount(order_total,tip_percentage):
    tip_amount=order_total*(tip_percentage/100)
    return round(tip_amount,2)


