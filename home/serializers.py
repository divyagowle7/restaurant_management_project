from rest_framework import serializers
from .models import MenuCategory,MenuItem,Ingredient,MenuItemIngrediet,Table,ContactFormSubmission
class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Ingredient
        fields=['id','name']
class DailySpecialSerializer(serializers.ModelSerializer):
    class Meta:
        model=MenuItem
        fields='__all__'
        
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

class TableSerializer(serializers,ModelSerializer):
    class Meta:
        model=Table
        fields=['table_number','capacity','is_availavle']      

class ContactFormSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model=ContactFormSubmission
        fields=['name','email','message']    