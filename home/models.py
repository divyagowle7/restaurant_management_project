from django.db import models
import random
from django.core.exceptions import ObjectDoesNotExist
# Create your models here.
class MenuCategory(models.Model):
    name = models.CharField(max_length=100,unique=True)
    is_featured=models.BooleanField(default=False)

    def __str__(self):
        return self.name
class MenuItem(models.Model):
    name=models.CharField(max_length=255)

class Ingredient(models.Model):
    name=models.CharField(max_length=255)

class MenuItemIngredient(models.Model):
    menu_item=models.ForeignKey(MenuItem,on_delete=models.CASCADE)
    ingredient=models.ForeignKey(Ingredient,on_delete=models.CASCADE)
    
class DailySpecial(models.Model):
    @staticmethod
    def get_random_special():
        try:
            count=DailySpecial.objects.count()
            if count==0:
                return None
            random_index=random.randint(0,count-1)
            return DailySpecial.objects.all()[random_index]
        except Exception as e:
            raise Exception(f"Error fetching random daily special: {str(e)}")     