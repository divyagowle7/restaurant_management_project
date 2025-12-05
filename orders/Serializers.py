from rest_framework import serializers
from .models import Order,OrderItem,PaymentMethod
from account.serializers import CustomerSerializer
from home.serializers import ItemSerializer

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=OrderItem
        fields=['product_name','quantity','price']

class OrderSerializer(serializers.ModelSerializer):
    items=OrderItemSerializer(many=True,read_only=True)
    customer=CustomerSerializer(read_only=True)
    order_items=ItemSerializer(many=True,read_only=True)

    class Meta:
        model=Order
        fields=['order_id','date','total_price','items','customer','order_items']
        
class PaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model=PaymentMethod
        fields='__all__'

class OrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields=['id','status']
        read_only_fields=['id']   

    def validate_status(self,value):
        if value not in [choice[0] for choice in Order.STATUS_CHOICES]:
            raise serializers.ValidationError("Invalid status provided.")
        return value