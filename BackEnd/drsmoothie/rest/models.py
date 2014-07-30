from django.db import models

# Nutrient model
class Nutrient(models.Model):
    id_nutrient = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    
# Ingredient Model
class Ingredient(models.Model):
    id_ingredient = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    
# User model
class User(models.Model):
    key = models.CharField(max_length=256)
    date_added = models.DateTimeField(auto_now_add=True)
    date_last_login = models.DateTimeField(auto_now_add=True) #time of the creation is the last login by default
    
# Recipe model
class Recipe (models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    timeAdded = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)


# this table creates the many to many relationship between Ingredient and Nutrient
class NutrIngrMap(models.Model):
    nutrient = models.ForeignKey(Nutrient)
    ingredient = models.ForeignKey(Ingredient)
    
    
    # this method is a safe way to create Nutrient - Ingredient relations so that 
    # we can avoid duplicated in the table. 
    # TODO : needs testing
    def create(self, nutrient, ingredient):
        
        # test if the entry already exists
        q = NutrIngrMap.objects.filter(Q(nutrient__exact=nutrient) & Q(ingredient__exact=ingredient))
        
        if q.count() > 0:
            r = NutrIngrMap(nutrient = nutrient, ingredient = ingredient)
        else:
            r = q  # there should only be one entry
        return r
    

#this model keeps track of which users recommended which recipes
class RecipeUserRecommendationsMap(models.Model):
    user = models.ForeignKey(User)
    recipe = models.ForeignKey(Recipe)

    # TODO: implement a create method like in the NutrIngrMap that only
    # creates a new entry if the requested entry does not exist
    
    
    
#test - added to the nutrient and ingredient models

#Orange -   1
#Lemon -    2
#Apple -    3

#vitamin C    1