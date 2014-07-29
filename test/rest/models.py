from django.db import models

# Create your models here.
class Nutrient(models.Model):
    name = models.CharField(max_length=100)
    
class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    nutrients = models.CharField(max_length=100)
    
    
