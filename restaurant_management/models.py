# Import the models module from Django's database package
from django.db import models

# Define a model for menu categories
class MenuCategory(models.Model):
    # Field to store the name of the menu category
    name=models.CharField(
        max_length=100, # Maximum length of the category name
        unique=True # Ensure category names are unique
        )
        
        # Define a string representation of the model instance
        def __str__(self):
            # Return the name of the menu category as its string representation
            return self.name