from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Coupon
from datetime import date

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
            