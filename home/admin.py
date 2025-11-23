from django.contrib import admin
from .models import Restaurant
# Register your models here.
class RestaurantAdmin(admin.ModelAdmin):
    list_display=('name','address','phone_number','email')
    search_fields=('name','address')
    list_filter=('is_active')
admin.site.register(Restaurant,RestaurantAdmin)

