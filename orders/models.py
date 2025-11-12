from django.db import models

# Create your models here.
class Coupon(models.Model):
    code=models.CharField(max_length=50,unique=True)
    discount_percentage=models.DecimalField(max_digits=4,decimal_places=2)
    is_active=models.BooleanField(default=True)
    valid_from=models.DateField()
    valid_until=models.DateField()

    def __str__(self):
        return self.code

class OrderStatus(models.Model):
    name=models.CharField(max_length=50,unique=True)
    status=models.ForiegnKey(OrderStatus,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.name