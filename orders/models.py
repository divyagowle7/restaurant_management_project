from django.db import models
from accounts.models import Customer
from home.models import Item,MenuItem
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
    status=models.CharField(max_length=20,choices=[
        ('Pending','Pending'),
        ('Processing','Processing'),
        ('Completed','Completed'),
        ('Cancelled','Cancelled'),
    ], default='Pending')
    status=models.CharField(max_length=10,choices=STATUS_CHOICES,default='Pending')
    def get_unique_item_names(self):
        unique_names=set(
            order_item.menu_item.name
            for order_item in self.orderitem_set.all()
        )
        return list(unique_names)

    def calculate_total(self):
        return sum(item.get_cost() for item in self.items.all())

class OrderItem(models.Model):
    order=models.ForiegnKey(Order,on_delete=models.CASCADE/,related_name='items')
    menu_item=models.ForiegnKey('MenuItem',on_delete=models.CASCADE)
    quantity=models.IntegerField()

    def get_cost(self):
        return self.menu_item.price*self.quantity

class MenuItem(models.Model):
    name=models.CharField(mal=255)

class PaymenttMethod(models.Model):
    name=models.CharField(max_length=255,unique=True)
    description=models.TextField(blank=True,null=True)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.name  
    