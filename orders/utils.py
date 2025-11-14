import secrets
import string
from datetime import date,time
from .models import Coupon.Order
from DailyOperatingHours import DailyOperatingHours
from django.db.models import Model,Sum


def generate_coupon_code(length=10,model=None,field='code'):
    """Generate a unique alphanumeric coupon code."""
    if not isinstance(length,int)or length<=0:
        return ValueError("Length must be a positive integer")
    characters=string.ascii_uppercase+string.ascii_lowercase+string.digits
    while True:
        code=''.join(secrets.choice(characters) for _ in range(length))
        if model is None or not model.objects.filter(**{field: code}).exists():
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

def get_daily_sales_total(date):
    total=Order.objects.filter(created_at_date=date).aggregate(total_sum=Sum('total_price'))['total_sum']or 0
    return total
