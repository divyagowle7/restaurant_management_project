from django.urls import path,include
from .views import CouponValidationView,OrderHistoryView,OrderRetrieveView,PaymentMethodList,OrderStatusUpdateView

urlpatterns = [
    path('coupons/validate/',CouponValidationView.as_view(),name='coupon_validate'),
    path('order-history/',OrderHistoryView.as_view(),name='order-history'),
    path('orders/<int:order_id>/',OrderRetrieveView.as_view()),
    path('payment-methods/',PaymentMethodList.as_view()),
    path('orders/<int:id>/status/',OrderStatusUpdateView.as_view(),name='update-order-status'),
    path('api/',include('orders.urls')),
]