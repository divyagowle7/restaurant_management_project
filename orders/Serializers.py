from rest_framework import serializers
from .models import Order,OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=OrderItem
        fields=['product_name','quantity','price']

class OrderSerializer(serializers.ModelSerializer):
    items=OrderItemSerializer(many=True,read_only=True)
    class Meta:
        model=Order
        fields=['order_id','date','total_price','items']
