from django.http import HttpResponse
from models import *
from django.core import serializers
import json
# Create your views here.


def ingredient(request):
    ingredients = Ingredient.objects.all()
    
    return HttpResponse(serializers.serialize("json", ingredients))

def nutrients_of_an_ingredient(request):
    nutrient = Nutrient.objects.get(pk=request.GET['id'])
    
    related_ingredients = NutrIngrMap.objects.filter(id_nutrient__exact = nutrient);
    
    ingredients = list()
    for ingr in related_ingredients:
        ingredients.append(ingr.id_ingredient)
    #ingredients = Ingredient.objects.filter(id_ingredient__in = related_ingredients)
    
    return HttpResponse(serializers.serialize("json", ingredients))
#    return HttpResponse(json.dumps(related_ingredients))