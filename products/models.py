from django.db import models
from home.models import MenuCategory
# Create your models here.
class Item(models.Model):
    item_name = models.CharField(max_length=150)
    item_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.item_name)

class NutritionalInformation(models.Model):
    menu_item=models.ForeignKey(MenuCategory,on_delete=models.CASCADE)
    calories=models.IntegerField()
    protien_grams=models.DecimalField(max_digits=5,decimal_places=2)
    fat_grams=models.DecimalField(max_digits=5,decimal_places=2)
    carbohydrate_grams=models.DecimalField(max_digits=5,decimal_places=2)

    def __str__(self):
        return f"{self.menu_item.name}:{self.calories} calories"
        