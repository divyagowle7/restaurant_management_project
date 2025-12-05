from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status,generics
from rest_framework.generics import RetrieveAPIView
from rest_framework.views import APIView
from .models import Coupon,Order,PaymentMethod
from datetime import date
from .utils import generate_coupon_code
from rest_framework.permissions import IsAuthenticated
from .serializers import OrderSeializer,PaymentMethodSerializer,OrderStatusSeializer

# Create your views here.
class CouponValidationView(APIView):
    def post(self,request):
        code=request.data.get('code')
        try:
            coupon=Coupon.objects.get(code=code)
            if coupon,is_active and coupon.valid_from <= date.today() <=coupon.valid_until:
                return Response({
                    'success': True,
                    'discount_percentage':coupon.discount_percentage
                })
            else:
                return Response({
                    'success':False,
                    'error':'Coupon is not active or has expired'
                },status=status.HTTP_400_BAD_REQUEST)
        except Coupon.DoesNotExist:
            return Response({
                'success':False
                'error':'Invalid coupon code'
            },status=status.HTTP_400_BAD_REQUEST)
    coupon_code=generate_coupon_code(8)
    print(coupon_code)

class OrderHistoryView(generics.ListAPIView):
    serializer_class=OrderSeializer
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

class OrderRetrieveView(RetrieveAPIView):
    queryset=Order.objects.all()
    serializer_class=OrderSeializer
    lookkup_field='order_id'

class CancelOrderView(generics.UpdateAPIView):
    queryset=Order.objects.all()
    serializer_class=OrderSeializer
    lookkup_field='id'

    def update(self,request,*args,**kwargs):
        try:
            order=self.get_object()
            if order.status=='Completed':
                return Response({'error';'Cannot cancel completed order'},status=status.HTTP_400_BAD_REQUEST)
            order.status='Cancelled'
            order.save()
            return Response({'message':'Order cancelled'},status=status.HTTP_200_OK)
        except Order.DoesNotExist:
            return Response({'error':'Order not found'},status=status.HTTP_404_NOT_FOUND)
class PaymentMethodList(generics.ListAPIView):
    queryset=PaymentMethod.objects.filter(is_active=True)
    serializer_class=PaymentMethodSerializer
                
class OrderStatusUpdateView(generics.UpdateAPIView):
    queryset=Order.objects.all()
    serializer_class=OrderStatusSeializer
    lookkup_field='id'

    def update(self,request,*args,**kwargs):
        instance=self.get_object()
        serializer=self.get_serailizer(instance,data=request.data,partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({'message':'Order status updated successfully'},status=status.HTTP_200_OK)
        