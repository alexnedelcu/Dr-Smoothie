from drsmoothie.rest.models import *
class DjModels:
	@staticmethod
	def addIngredient(id, name, type):
		typeObj, created = IngredientType.objects.get_or_create(type=type)
		
		if created:
			typeObj.save()
			
		i, created = Ingredient.objects.get_or_create(id=id, name=name, type=typeObj)
		
		if created:
			i.save()
		
		return i
		
	@staticmethod
	def addMeasurement(id, ingredient, portion, amount_grams):
		w, created = Measurement.objects.get_or_create(id = id, ingredient=ingredient, portion = portion, amount_grams = amount_grams)
		
		if created:
			w.save()
		return w
	
	@staticmethod
	def addUnits(id, description):
		p, created = Unit.objects.get_or_create(id=id, description=description)
		
		if created is True:
			p.save()
		
		return p
		
	@staticmethod
	def addNutrient(id, name, unit, decimals):
		n, created = Nutrient.objects.get_or_create(id=id, name=name, unit=unit, decimals=decimals)
		
		if created:
			n.save()
			
		return n

	@staticmethod
	def addNutrIngr(nutrient, ingredient):
		ni, created = NutrIngrMap.objects.get_or_create(nutrient=nutrient, ingredient=ingredient, quantity=100)
		
		if created:
			ni.save()
		
		return ni
	

class Helper:
	@staticmethod
	def findCorrespondingEntries(filename, colIndex, key):
		objects = list()
		f = open(filename, 'r')
		for line in f:
			line =  line.split('^')
			
			if line[colIndex] == key:
				objects.append(line)
		
		return objects

	@staticmethod
	def importWeightsPortions(ingredientByModel):
		weights = Helper.findCorrespondingEntries("../database_to_import/ascii/FoodWeights.txt", 0, ingredientByModel.id)

		for w in weights:
			print "\tweight ", w[0], w[3], w[6]
			p = Helper.findCorrespondingEntries("../database_to_import/ascii/FoodPortionDesc.txt", 0, w[3])
			print "\t\tportion for ", p[0][0], p[0][3]
			
			portionByModel = DjModels.addUnits(p[0][0], p[0][3])
			#weight = addMeasurement(id, ingredient, portion, amount_grams)
			weightByModel = DjModels.addMeasurement(w[0], ingredientByModel, portionByModel, w[6])
	
	@staticmethod
	def importNutrients(ingredientByModel):
		nutValMap = Helper.findCorrespondingEntries("../database_to_import/ascii/FNDDSNutVal.txt", 0, ingredientByModel.id)
		for nv in nutValMap:
			print "\tnutrient", nv[1], nv[4]
			
			# find the nutrient names, amounts and units by id
			nutrient = Helper.findCorrespondingEntries("../database_to_import/ascii/NutDesc.txt", 0, nv[1])
			print "\t\tnutr desc: ", nutrient[0][1], "^", nutrient[0][2], "^", nutrient[0][3], "^", nutrient[0][4]
			
			nutrientByModel = DjModels.addNutrient(nutrient[0][0], nutrient[0][1], nutrient[0][3], nutrient[0][4])
			nutrIngrByModel = DjModels.addNutrIngr(nutrientByModel, ingredientByModel)
		
	@staticmethod
	def importIngredientType(filename, type):
		f = open(filename, 'r')
		for iterator in range(0,10):
			line =  f.readline().split('^')
			food_id = line[0]
			food_name = line[3]

			print food_id, food_name
			ingredientByModel = DjModels.addIngredient(food_id, food_name, type)

			# get the portion sizes
			Helper.importWeightsPortions(ingredientByModel)
			
			# get the corresponging nutrients
			Helper.importNutrients(ingredientByModel)
		f.close()
		
Helper.importIngredientType('../database_to_import/ascii/MainFoodDesc_fruit_selection.txt', "fruit")
Helper.importIngredientType('../database_to_import/ascii/MainFoodDesc_vegetable_selection.txt', "vegetable")
Helper.importIngredientType('../database_to_import/ascii/MainFoodDesc_nut_selection.txt', "nuts")
Helper.importIngredientType('../database_to_import/ascii/MainFoodDesc_other_selection.txt', "other")