from datetime import datetime

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
    