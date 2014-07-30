from django.db import models

# Create your models here.
class Nutrient(models.Model):
    id_nutrient = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    
class Ingredient(models.Model):
    id_ingredient = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    
class NutrIngrMap(models.Model):
    id_nutrient = models.ForeignKey(Nutrient)
    id_ingredient = models.ForeignKey(Ingredient)
    
#test:
#Orange -   1
#Lemon -    2
#Apple -    3

#vitamin C    1