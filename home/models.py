from django.db import models
import random
from django.core.exceptions import ObjectDoesNotExist
from datetime import date
# Create your models here.
class MenuCategory(models.Model):
    name = models.CharField(max_length=100,unique=True)
    is_featured=models.BooleanField(default=False)

    def __str__(self):
        return self.name
class MenuItem(models.Model):
    category=models.CharField(max_length=100)
    name=models.CharField(max_length=255)
    description=models.TextField()
    price=models.DecimalField(max_digits=10,decimal-places=2)
    is_available=models.BooleanField(default=True)
    objects=MenuItemManager()

class Ingredient(models.Model):
    name=models.CharField(max_length=255)

class MenuItemIngredient(models.Model):
    menu_item=models.ForeignKey(MenuItem,on_delete=models.CASCADE)
    ingredient=models.ForeignKey(Ingredient,on_delete=models.CASCADE)
    
class DailySpecial(models.Model):
    date=models.DateField()
    objects=DailySpecialManager()
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
class DailySpecialManager(models.Manager):
    def upcoming(self):
        return self.filter(date__gte=date.today())
class MenuItemManager(models.Model):
    def get_top_selling_items(self,num_items=5):
        return self.annotate(
            order_count=models.Count('orderitem')
        ).order_by('-order_count')[:num_items]

class ContactFormSubmission(models.Model):
    name=models.CharField(max_length=255)
    email=models.EmailField()
    message=models.TextField()
    