from django.db import models
from django.db.models import Q

# Nutrient model
class Nutrient(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    unit = models.CharField(max_length=32)

# Ingredient Model
class Ingredient(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    unit = models.CharField(max_length=32)

# User model
class User(models.Model):
    key = models.CharField(max_length=256)
    date_added = models.DateTimeField(auto_now_add=True)
    date_last_login = models.DateTimeField(auto_now_add=True) #time of the creation is the last login by default
    
# Recipe model
class Recipe(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User)
    timeAdded = models.DateTimeField(auto_now_add=True)
    
    @staticmethod
    def create(name, user):
        # test if the entry already exists
        try:
            r = Recipe.objects.get(name__exact=name)
        except:
            r = Recipe(name=name,user=user)
            r.save()
        return r

# Relationship Mappings
# this table creates the many to many relationship between Ingredient and Nutrient
class NutrIngrMap(models.Model):
    nutrient = models.ForeignKey(Nutrient)
    ingredient = models.ForeignKey(Ingredient)
    quantity = models.FloatField()
    
    # this method is a safe way to create Nutrient - Ingredient relations so that 
    # we can avoid duplicated in the table. 
    # TODO : needs testing
    def create(self, nutrient, ingredient):
        # test if the entry already exists
        q = NutrIngrMap.objects.filter(Q(nutrient__exact=nutrient) & Q(ingredient__exact=ingredient))
        
        if q.count() is 0:
            r = NutrIngrMap(nutrient = nutrient, ingredient = ingredient)
        else:
            r = q  # there should only be one entry
        return r
    
#this model represents the mapping of what ingredients a recipe contains
class RecipeIngrMap(models.Model):
    recipe = models.ForeignKey(Recipe)
    ingredient = models.ForeignKey(Ingredient)
    quantity = models.FloatField()

    @staticmethod
    def create(recipe, ingredient, quantity):
        # test if the entry already exists
        q = RecipeIngrMap.objects.filter(Q(recipe__exact=recipe) & Q(ingredient__exact=ingredient))
        
        # if RecipeIngrMap doesn't exist, create one
        # else return the existing mapping
        if q.count() is 0:
            r = RecipeIngrMap(recipe=recipe,ingredient=ingredient,quantity=quantity)
            r.save()
        else:
            r = q  # there should only be one entry
        # returns the RecipeIngrMap
        return r

#this model keeps track of which users recommended which recipes
class RecipeUserRecommendationsMap(models.Model):
    recipe = models.ForeignKey(Recipe)
    user = models.ForeignKey(User)

    # TODO: test if this works properly
    def create(self, recipe, user):
        # test if the entry already exists
        q = RecipeUserRecommendationsMap.objects.filter(Q(recipe__exact=recipe) & Q(user__exact=user))
        
        if q.count() is 0:
            r = RecipeUserRecommendationsMap(recipe=recipe, user=user)
        else:
            r = q  # there should only be one entry
        return r
    
    
    