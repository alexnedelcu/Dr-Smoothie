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

def CreateRecommendationCountList(recipes):
	reclist = []
	for r in recipes:
		reccount = RecipeUserRecommendationsMap.objects.filter(recipe__exact=r).count()
		reclist.append(reccount)

	return reclist

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

def ConvertIngredientsToJson(ingredients):
	jsonlist = []
	measurementjson = []
#	nutringrmapjson = []
	nutrientlists = []
	unitsjson = []
	for ingr in ingredients:
		units = []
		nutrilist = []
		
		measurements = Measurement.objects.filter(ingredient=ingr)
		mapping = NutrIngrMap.objects.filter(ingredient=ingr)
		for m in measurements:
			unit = m.unit
			units.append(unit)
			
		for m in mapping:
			nutrilist.append(m.nutrient)
		
		unitsjson.append(SerializeAndLoad(units))
		measurementjson.append(SerializeAndLoad(measurements))
		nutrientlists.append(SerializeAndLoad(nutrilist))

	ingrjson = SerializeAndLoad(ingredients)

	# ingr -ingredient json
	# wgts - json list of Measurements
	# nutrs - json list of Nutrients
	#for ingr, mnts, nimaps in itertools.izip(ingrjson, measurementjson, nutringrmapjson):
	for ingr, mnts, nutrs, units in itertools.izip(ingrjson, measurementjson, nutrientlists, unitsjson):
		newjson = ingr["fields"]#["fields"]
		newjson["id"] = ingr["pk"]
		newjson["name"] = ingr["fields"]["name"]

		jsonunits = []
		for u in units:
			fields = u["fields"]
			ujson = fields
			ujson["id"] = u["pk"]
			jsonunits.append(ujson)

		#for m in mnts:
		#	mfields = m["fields"]
			#mjson = mfields["portion"]["fields"]
		#	mjson = mfields["unit"]["fields"]
		#	unitsjson.append(mjson)

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

		newjson["units"] = jsonunits
		newjson["nutrient"] = nutrilistjson

		jsonlist.append(newjson)

	# usable json
	return json.dumps(jsonlist)

# takes in a django retrieved list of nutrients
# converts into json format for how the frontend wants it
def ConvertNutrListToJsonList(nutrlist):
	jsonlist = []
	encoded = SerializeAndLoad(nutrlist)

	for e in encoded:
		njson = e["fields"]
		njson["id"] = e["pk"]
		jsonlist.append(njson)

	return json.dumps(jsonlist)

# This is for converting a single recipe into json
def ConvertRecipeToJson(recipe, ingrmaplist, recs):
	djangojson = serializers.serialize("json", [recipe])
	encoded = json.loads(djangojson)

	newjson = encoded[0]["fields"]
	newjson["id"] = encoded[0]["pk"]
	newjson["ingredients"] = ConvertModelToJsonList(ingrmaplist)
	newjson["recs"] = recs

	return json.dumps(newjson)

# must have a list of integers that represent number of recommendations.
# converts a list of recipes into a recipelist.
def ConvertRecipeToJsonList(recipelist, reclist):
	jsonlist = []
	encoded = SerializeAndLoad(recipelist)
	
	for e, rec in itertools.izip(encoded, reclist):
		rjson = e["fields"]
		rjson["id"] = e["pk"]
		rjson["recs"] = rec
		jsonlist.append(rjson)

	return json.dumps(jsonlist)

# 
# def ConvertIngrMapToJsonList(modellist):
# 	jsonlist = []
# 	encoded = SerializeAndLoad(modellist)

# 	for e in encoded:
# 		fields = e["fields"]
# 		ingr = fields["ingredient"]
# 		newjson = ingr["fields"]
# 		newjson["id"] = ingr["pk"]
# 		newjson["quantity"] = fields["quantity"]
# 		jsonlist.append(newjson)
# 	return json.dumps(jsonlist)

# return value = [{
# 	"id" : "ingrid",
# 	"name" : "ingrname",
# 	"id" : "the ID",
# 	"quantity" : "quantity"
# }, ...]

#def ConvertRecipeToJsonList2(recipelist):
#	jsonlist = []
#	recdict = {}
#	for r in recipelist:
#		recs = RecipeUserRecommendationsMap.objects.filter(recipe__exact)
		# recdict[str(r.pk)] = recs
	
	# encoded = SerializeAndLoad(recipelist)

	# for e in encoded:
	# 	rid = e["pk"]
	# 	newjson = e["fields"]
	# 	newjson["id"] = rid
	# 	newjson[rid] = recdict[rid]
	# 	jsonlist.append(newjson)

	# return json.dumps(jsonlist)



	