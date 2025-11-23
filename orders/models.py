from django.db import models
from accounts.models import Customer
from home.models import Item
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

class Order(models.Model):
    order_id=models.AutoField(primary_key=True)
    customer=models.ForiegnKey(Customer,on_delete=models.CASCADE)
    order_items=models.ManyToManyField(Item)
    total_price=models.DecimalField(max_digits=10,decimal_places=2)
    STATUS_CHOICES=[
        ('Pending','Pending'),
        ('Processed',Processed),
    ]
    status=models.CharField(max_length=10,choices=STATUS_CHOICES,default='Pending')
    def get_unique_item_names(self):
        unique_names=set(
            order_item.menu_item.name
            for order_item in self.orderitem_set.all()
        )
        return list(unique_names)

class OrderItem(models.Model):
    order=models.ForiegnKey(Order,on_delete=models.CASCADE)
    menu_item=models.ForiegnKey('MenuItem',on_delete=models.CASCADE)

class MenuItem(models.Model):
    name=models.CharField(mal=255)
    
    