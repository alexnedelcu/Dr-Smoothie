from django.http import HttpResponse
from models import *
from django.core import serializers
import json
# Create your views here.


def ingredient(request):
    ingredients = Ingredient.objects.all()
    
    return HttpResponse(serializers.serialize("json", ingredients))

def ingredients_with_a_nutrient(request):
    
    # look for the input nutrient, specified in the URL
    # e.g. http://localhost:8000/nutr_of_ingr?id=1
    nutrient = Nutrient.objects.get(pk=request.GET['id'])
    
    # get all the corresponding ingredients
    related_ingredients = NutrIngrMap.objects.filter(nutrient__exact = nutrient);
    
    # build a list of the corresponding ingredient (useful so it can be serialized in json)
    ingredients = list()
    for ingr in related_ingredients:
        ingredients.append(ingr.ingredient)
    
    return HttpResponse(serializers.serialize("json", ingredients))