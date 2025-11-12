import secrets
import string
from .models import Coupon # Assuming you have a coupon

def generate_coupon_code(length=10):
    """
    Generate a unique alphanumeric coupon code.
    """
    characters=string.ascii_letters+string.digits
    while True:
        code=''.join(secrets.choice(characters) for _ in range(length))
        if not Coupon.objects.filter(code=code).exists():
            return code

