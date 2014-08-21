from drsmoothie.rest.models import *

def findCorrespondingEntries(filename, colIndex, key):
	objects = list()
	f = open(filename, 'r')
	for line in f:
		line =  line.split('^')
		
		if line[colIndex] == key:
			objects.append(line)
	
	return objects

def truncateAllTables():
	Ingredient.objects.all().delete()
	Weight.objects.all().delete()
	Portion.objects.all().delete()
	Nutrient.objects.all().delete()
	NutrIngrMap.objects.all().delete()

def addIngredient(id, name):
	i = Ingredient()
	i.id = id
	i.name=name
	i.save()
	return i
	
def addWeight(id, ingredient, portion, amount_grams):
	w, created = Weight.objects.get_or_create(id = id, ingredient=ingredient, portion = portion, amount_grams = amount_grams)
	
	if created:
		w.save()
	return w
	
def addPortion(id, description):
	p, created = Portion.objects.get_or_create(id=id, description=description)
	
	if created is True:
		p.save()
	
	return p
	
def addNutrient(id, name, unit, decimals):
	n, created = Nutrient.objects.get_or_create(id=id, name=name, unit=unit, decimals=decimals)
	
	if created:
		n.save()
		
	return n

def addNutrIngr(nutrient, ingredient):
	ni, created = NutrIngrMap.objects.get_or_create(nutrient=nutrient, ingredient=ingredient, quantity=100)
	
	if created:
		ni.save()
	
	return ni
	
# truncate all teh tables
#truncateAllTables()

# this script doesnt work because it needs user instance 
f = open('../database_to_import/ascii/MainFoodDesc.txt', 'r')
for iterator in range(0,5):
	line =  f.readline().split('^')
	food_id = line[0]
	food_name = line[3]

	print food_id, food_name
	ingredientByModel = addIngredient(food_id, food_name)

	# get the portion sizes
	weights = findCorrespondingEntries("../database_to_import/ascii/FoodWeights.txt", 0, food_id)

	for w in weights:
		print "\tweight ", w[0], w[3], w[6]
		p = findCorrespondingEntries("../database_to_import/ascii/FoodPortionDesc.txt", 0, w[3])
		print "\t\tportion for ", p[0][0], p[0][3]
		
		portionByModel = addPortion(p[0][0], p[0][3])
		#weight = addWeight(id, ingredient, portion, amount_grams)
		weightByModel = addWeight(w[0], ingredientByModel, portionByModel, w[6])
		
	# get the corresponging nutrients
	nutValMap = findCorrespondingEntries("../database_to_import/ascii/FNDDSNutVal.txt", 0, food_id)
	for nv in nutValMap:
		print "\tnutrient", nv[1], nv[4]
		
		# find the nutrient names, amounts and units by id
		nutrient = findCorrespondingEntries("../database_to_import/ascii/NutDesc.txt", 0, nv[1])
		print "\t\tnutr desc: ", nutrient[0][1], "^", nutrient[0][2], "^", nutrient[0][3], "^", nutrient[0][4]
		
		nutrientByModel = addNutrient(nutrient[0][0], nutrient[0][1], nutrient[0][3], nutrient[0][4])
		nutrIngrByModel = addNutrIngr(nutrientByModel, ingredientByModel)
		
	
f.close()
