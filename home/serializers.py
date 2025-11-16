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
        fields=['id','name','ingredients']
        
class MenuCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=MenuCategory
        fields='__all__'
        
        