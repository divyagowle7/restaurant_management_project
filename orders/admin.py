from django.contrib import admin
from .models import Coupon,Order

# Register your models here.
def mark_orders_processed(modeladmin,request,queryset):
    queryset.update(status='Processed')
    mark_orders_processed.short_description='Mark selected orders as Processed'

class OrderAdmin(admin.ModelAdmin):
    list_display=['id','status']
    actions=[mark_orders_processed]

admin.site.register(Coupon,Order,OrderAdmin)
