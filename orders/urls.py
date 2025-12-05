from django.urls import path
from .views import CouponValidationView,OrderHistoryView,OrderRetrieveView,PaymentMethodList

urlpatterns = [
    path('coupons/validate/',CouponValidationView.as_view(),name='coupon_validate'),
    path('order-history/',OrderHistoryView.as_view(),name='order-history'),
    path('orders/<int:order_id>/',OrderRetrieveView.as_view()),
    path('payment-methods/',PaymentMethodList.as_view()),
]