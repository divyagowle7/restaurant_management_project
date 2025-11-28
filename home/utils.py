from datetime import datetime
from django.core.mail import send_mail
from django.conf import settings

def is_restaurant_open():
    # Define opening hours (Monday=0,Sunday=6)
    opening_hours={
        0:(9,22), # Monday: 9AM - 10PM
        1:(9,22), # Tuesday: 9AM -10PM
        2:(9,22), # Wednesday: 9AM - 10PM
        3:(9,22), # Thrusday: 9AM - 10PM
        4:(9,23), # Friday: 9AM - 11PM
        5:(10,23), # Saturday: 10AM - 11PM
        6:(10,22), # Sunday: 10AM - 10PM
    }
    now = datetime.now()
    current_day = now.weekday()
    current_hour = now.hour

    open_hour,close_hour = opening_hours[current_day]
    return open_hour <= current_hour < close_hour
def send_order_confirmation_email(order_id,customer_email,**kwargs):
    try:
        subject=f"Order confirmation:{order_id}"
        message=f"Dear customer,your order {order_id} has been confirmed 
        send_mail(subject,message,settings.DEFAILT_FROM_EMAIL,[customer_email],fail_silently=False)
    except Exception as e:
        print(f"Error sending email:{e}")
        return False 