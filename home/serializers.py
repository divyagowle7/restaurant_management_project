from rest_framework import serializers
from .models import MenuCategory,MenuItem,Ingredient,MenuItemIngrediet

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Ingredient
        fields=['id','name']

class MenuItemSerializer(serializers.ModelSerializer):
    ingredients=IngredientSerializer(many=True,read_only=True)
    class Meta:
        model=MenuItem
        fields=['id','name','description','price','is_available']
    def validate_price(self,value):
        if vakue<=0:
            raise serializers.ValidationError("Price must be a positive number")
        return value
        
class MenuCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=MenuCategory
        fields='__all__'
        
        