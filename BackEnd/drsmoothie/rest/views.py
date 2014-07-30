from django.http import HttpResponse
from models import *
from django.core import serializers
# Create your views here.


def ingredient(request):
    ingredients = Ingredient.objects.all()
    return HttpResponse(serializers.serialize("json", ingredients))
#    return HttpResponse("Should be replaced by the ingredients JSON")