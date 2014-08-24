import json
import sys
from models import *
from django.core import serializers
from django.db import models
import itertools



	
# parsing data from django style json
#{
	# pk: pk
	# fields: { model data needed }
#}


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
	measurementjson = []
	nutringrmapjson = []
	nutrientlists = []
	for ingr in ingredients:
		measurements = SerializeAndLoad(Measurement.objects.filter(ingredient=ingr))
		#measurements = SerializeAndLoad(Weight.objects.filter(ingredient=ingr))
		measurementjson.append(measurements)

		mapping = NutrIngrMap.objects.filter(ingredient=ingr)
		nutrilist = []
		for m in mapping:
			nutrilist.append(m.nutrient)
		
		#nutringrmapjson.append(nutringrtemp)
		nutrientlists.append(SerializeAndLoad(nutrilist))

	ingrjson = SerializeAndLoad(ingredients)
	jsonlist = []

	# ingr -ingredient json
	# wgts - json list of Measurements
	# nutrs - json list of Nutrients
	#for ingr, mnts, nimaps in itertools.izip(ingrjson, measurementjson, nutringrmapjson):
	for ingr, mnts, nutrs in itertools.izip(ingrjson, measurementjson, nutrientlists):
		newjson = ingr["fields"]#["fields"]
		newjson["id"] = ingr["pk"]
		newjson["name"] = ingr["fields"]["name"]

		unitsjson = []
		for m in mnts:
			mfields = m["fields"]
			#mjson = mfields["portion"]["fields"]
			mjson = mfields["unit"]["fields"]
			unitsjson.append(mjson)

		nutrilistjson = []
		for nt in nutrs:
			njson = nt["fields"]
			njson["id"] = nt["pk"]
			nutrilistjson.append(njson)

#		nutrjson = []
#		for nim in nimaps:
#			nutr = nim["fields"]
#			njson = nutr
#			njson["id"] = nutr["nutrient"]["pk"]
#			njson["name"] = nutr["nutrient"]["fields"]["name"]
#			nutrjson.append(njson)

		newjson["units"] = unitsjson
		newjson["nutrient"] = nutrilistjson
		#newjson["nutrients"] = nutrijson

		jsonlist.append(newjson)

	# usable json
	return json.dumps(jsonlist)

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
