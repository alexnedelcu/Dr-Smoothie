from drsmoothie.rest.models import *

f = open('../database_to_import/ascii/NutDesc.txt', 'r')  
for line in f:  
   line =  line.split('^')  
   nutrient = Nutrient()  
   nutrient.id_nutrient = line[0]
   nutrient.name = line[1]   
   nutrient.unit = line[3]
   nutrient.save()  

f.close()  

#just for testing
user = User()
user.key = 1 
user.save()

# this script doesnt work because it needs user instance 
f = open('../database_to_import/ascii/MainFoodDesc.txt', 'r')
for line in f:
   line =  line.split('^')
   recipe = Recipe()
   recipe.id = line[0]
   recipe.name = line[3]
   recipe.user = user
   recipe.save()

f.close()




f = open('../database_to_import/ascii/AddFoodDesc.txt', 'r')
for line in f:
   line =  line.split('^')
   ingredient = Ingredient()
   ingredient.id_ingredient = line[0]
   ingredient.name = line[3]
   ingredient.save()

f.close()
