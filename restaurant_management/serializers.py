from rest_frameworks import serializers
from .models import MenuCategory
class MenuCategorySeializer(serializers.ModelSerializer):
    class Meta:
        model=MenuCategory
        fields=['name']