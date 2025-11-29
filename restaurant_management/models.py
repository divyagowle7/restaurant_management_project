from django.db import models
class Restaurant(models.Model):
    has_deliver=models.BooleanField(default=False)
    opening_days=models.CharField(max_length=50)
    