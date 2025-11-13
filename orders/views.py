from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status,generics
from rest_framework.views import APIView
from .models import Coupon,Order
from datetime import date
from .utils import generate_coupon_code
from rest_framework.permissions import IsAuthenticated
from .serializers import OrderSeializer

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
