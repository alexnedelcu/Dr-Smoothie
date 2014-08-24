import json
import sys
from models import *
from django.core import serializers
from django.db import models
import itertools

def SerializeAndLoad(modellist):
	jsonlist = serializers.serialize("json", modellist)
	return json.loads(jsonlist)

# serialize a list of django style json
# into json we need for the frontend
# list is a result of 
# serializers.serialize("json", modellist)
def ConvertModelToJsonList(modellist):
	jsonlist = []
	djangojson = serializers.serialize("json", modellist)
	encoded = json.loads(djangojson)

	for e in encoded:
		newjson = e["fields"]
		newjson["id"] = e["pk"]
		jsonlist.append(newjson)
	return json.dumps(jsonlist)

#for f,b in itertools.izip(foo,bar):
#    print(f,b)
# takes in a list of ingredients
# e.g. (Ingredient.objects.all())
def ConvertIngredientsToJson(ingredients):
	jsonlist = []
	weightjson = []
	nutringrmapjson = []
	for ingr in ingredients:
		weights = Weight.objects.filter(ingredient_exact=ingr)
		weightjson.append(SerializeAndLoad(weights))
		nutringrtemp = SerializeAndLoad(NutrIngrMap.objects.filter(ingr_exact=ingr))
		nutringrjson.append(nutringrtemp)
		
	ingrjson = SerializeAndLoad(ingredients)

	for i, w in itertools.izip(ingrjson, weightjson):
		newjson = i["fields"]
		newjson["units"] = 

	# parsing data from django style json
	#{
		# pk: pk
		# fields: { model data needed }
	#}

def ConvertIngrMapToJsonList(modellist):
	jsonlist = []
	djangojson = serializers.serialize("json", modellist)
	encoded = json.loads(djangojson)

	for e in encoded:
		fields = e["fields"]
		ingr = fields["ingredient"]
		newjson = ingr["fields"]
		newjson["id"] = ingr["pk"]
		newjson["quantity"] = fields["quantity"]
		jsonlist.append(newjson)
	return json.dumps(jsonlist)

def ConvertRecipeToJsonList(recipelist):
	jsonlist = []
	recdict = {}
	for r in recipelist:
		recs = RecipeUserRecommendationsMap.objects.filter(recipe__exact)
		recdict[str(r.pk)] = recs
	
	djangojson = serializers.serialize("json", recipelist)
	encoded = json.loads(djangojson)
	for e in encoded:
		rid = e["pk"]
		newjson = e["fields"]
		newjson["id"] = rid
		newjson[rid] = recdict[rid]
		jsonlist.append(newjson)
	return json.dumps(jsonlist)


def ConvertRecipeToJson(recipe, ingrmaplist, recs):
	djangojson = serializers.serialize("json", [recipe])
	encoded = json.loads(djangojson)
	newjson = encoded[0]["fields"]
	newjson["id"] = encoded[0]["pk"]
	newjson["ingredients"] = ConvertModelToJsonList(ingrmaplist)
	newjson["recs"] = recs

	return json.dumps(newjson)
