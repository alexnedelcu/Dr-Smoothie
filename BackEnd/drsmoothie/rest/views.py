from django.http import HttpResponse
from models import *
from django.core import serializers
from django.db import models
from utils import *
# This is not necessary
#from django.views.decorators.csrf import csrf_protect
#from django.core.context_processors import csrf
import json
import sys
import os
# Create your views here.

# GET Requests
def GetIngredient(request):
    retrievedIngredient = Ingredient.objects.get(pk=request.GET['id'])
    
    #Ingredient.objects.get(pk=request.GET['id'])
    return HttpResponse(serializers.serialize("json", [retrievedIngredient]))

# /Ingredients
def Ingredients(request):
    ingredients = Ingredient.objects.all()
    #djangojson = serializers.serialize("json", ingredients)
    jsonlist = ConvertModelToJsonList(ingredients)

    return HttpResponse(jsonlist)

# /Nutrients
def Nutrients(request):
    nutrients = Nutrient.objects.all()
    #djangojson = serializers.serialize("json", nutrients)
    jsonlist = ConvertModelToJsonList(nutrients)

    return HttpResponse(jsonlist)

# /IngredientByRecipe?id=[value]
def IngredientsByRecipe(request):
    recipeid = str(request.GET["id"])
    ingrlist = []
    try:
        recipe = Recipe.objects.get(pk=recipeid)
        recipemappings = RecipeIngrMap.objects.filter(recipe__exact=recipe)

    except:
        ingrlist = []
    return HttpResponse(ConvertIngrMapToJsonList(recipemappings))

#/Recipe?id=[value]
def GetRecipe(request):
    djson = []
    try:
        ingrlist = []
        recipe = Recipe.objects.get(pk=request.GET["id"])
        recipemappings = RecipeIngrMap.objects.filter(recipe__exact=recipe)
        for rm in recipemappings:
            ingrlist.append(rm.ingredient)
        recs = RecipeUserRecommendationsMap.objects.filter(recipe__exact=recipe)
        djson = ConvertRecipeToJson(recipe, ingrlist, recs.count())
        
    except:
        djson = []
    return HttpResponse(djson)

# Not needed for client
# /Users
def Users(request):
    users = User.objects.all()
    #djangojson = serializers.serialize("json", users)
    jsonlist = ConvertModelToJsonList(users)

    return HttpResponse(jsonlist)

#TODO reformat response
# /IngredientsByNutrient?id=[val]
def IngredientsByNutrient(request):    
    # look for the input nutrient, specified in the URL
    # e.g. http://localhost:8000/GetIngredientsByNutrient?id=1
    nutrient = Nutrient.objects.get(pk=request.GET['id'])
    
    # get all the corresponding ingredients
    related_ingredients = NutrIngrMap.objects.filter(nutrient__exact = nutrient);
    
    # build a list of the corresponding ingredient (useful so it can be serialized in json)
    ingredients = list()
    for ingr in related_ingredients:
        ingredients.append(ingr.ingredient)

    #djangojson = serializers.serialize("json", ingredients)
    jsonlist = ConvertModelToJsonList(ingredients)
    return HttpResponse(jsonlist)

# TODO json formatting
# /RecipesByUser?userkey=[sample userkey]
def RecipesByUser(request):
    try:
        userfound = User.objects.get(key=request.GET['userkey'])
        recipes = Recipe.objects.filter(user__exact = userfound)
    except User.DoesNotExist:
        recipes = []
    
    return HttpResponse(ConvertModelToJsonList(recipes))
    
# TODO json formatting
# /FavoriteRecipes
def FavoriteRecipes(request):
    try:
        userfound = User.objects.get(key=request.GET['userkey'])
        favorites = RecipeUserRecommendationsMap.objects.filter(user__exact=userfound)
    except:
        userfound = None
        favorites = []
    
    return HttpResponse(serializers.serialize("json", favorites))

# TODO
# -json formatting
# -finish the sorting
# /TopRecipes?start=[int]&end=[int]
def TopRecipes(request):
    recipes = Recipe.objects.all()
    start = int(request.GET['start'])
    end = int(request.GET['end'])
    rlist = []

    for r in recipes:
        recommendations = len(RecipeUserRecommendationsMap.objects.filter(recipe=r))
        rlist.append((r,recommendations))

    #list.sort(rlist, key=lambda tup: tup[1])
    sorted(rlist,key=lambda x: x[1])
    #for pair in rlist:
    #   serializers.serialize("json", pair)
    #serializers.serialize("json", rlist[start:end])
    return HttpResponse(serializers.serialize("json", recipes[0]))

# /Search/Ingredient?name=[str]
def SearchByIngredient(request):
    ingrname = str(request.GET['name'])
    ingrlist = Ingredient.objects.all()
    
    found = None
    for i in ingrlist:
        if ingrname.lower() == str(i.name).lower():
            found = i
            break
    
    if found is None:
        return HttpResponse('No results found.')
    else:
        recipes = []
        rmapping = RecipeIngrMap.objects.filter(ingredient__exact=found)
        
        # adds in a recipe if it isn't already in the list 
        for rm in rmapping:
            recipes.append(rm.recipe)
        return HttpResponse(ConvertModelToJsonList(recipes))


# /Search/Nutrient?name=[str]
def SearchByNutrient(request):
    nutriname = str(request.GET['name'])
    nutrilist = RecipeIngrMap.objects.all()
    
    nutrifound = None
    for n in nutrilist:
        if nutriname.lower() == str(n.name).lower():
            nutrifound = n
            break
    if nutrifound is None:
        return HttpResponse('No results found.')
    else:
        nutriIngrMapping = NutrIngrMap.objects.filter(nutrient__exact=nutrifound)
        recipes = []
        for ni in nutriIngrMapping:
            templist = RecipeIngrMap.objects.filter(ingredient__exact=ni.ingredient)
            
            # adds in a recipe if it isn't already in the list 
            for temp in templist:
                if not temp.recipe in recipes:
                    recipes.append(temp.recipe)

        return HttpResponse(ConvertModelToJsonList(recipes))

# TODO not even started
# /Search/Recipe?name=[str]
def SearchRecipe(request):
    recipename = str(request.GET['name'])
    recipefound = Recipe.objects.all()

    slist = []
    for r in recipefound:
        if recipename.lower() in str(r.name).lower():
            slist.append(r)
    
    return HttpResponse(ConvertModelToJsonList(slist))

# POST/PUT/UPDATE
# /AddRecipe
# request.body = (SampleRequestData.json)
def AddRecipe(request):
    data = json.loads(request.body)

    # retrieve needed data from data
    recipename = str(data["name"])
    ingredients = data["ingredients"]
    userkey = str(data["userkey"])

    # userfound should have a try statement
    try:
        userfound = User.objects.get(key=userkey)
    except:
        userfound = None
    if userfound is not None:    
        try:
            addedrecipe = Recipe.create(recipename, userfound)
        except:
            return HttpResponse('already exists')
        for ingr in ingredients:
            quantity = float(ingr["quantity"])
            ingrid = str(ingr["ingr_id"])
            ingrRetrieved = Ingredient.objects.get(pk=ingrid)
            rim = RecipeIngrMap.create(addedrecipe,ingrRetrieved,quantity)

    return HttpResponse('')

# TODO: handle exceptions and null user
# format response
# /AddUser
# request.body = (SampleRequestData.json)
def AddUser(request):
    data = json.loads(request.body)
    try:
        newuserkey = str(data["userkey"])
        userexists = User.objects.get_or_create(key=newuserkey)
        responseMessage = 'User was created or already exists'
    except:
        responseMessage = 'User was not created.'

    return HttpResponse(responseMessage)

# TODO: handle exceptions and null user
# format response
# /RecommendRecipe?recipeid=[val]&userkey=[val]
def RecommendRecipe(request):
    try:
        recipeRecommend = Recipe.objects.get(pk=request.GET['recipeid'])
        userRecommend = User.objects.get(key=request.GET['userkey'])

        RecipeUserRecommendationsMap.create(recipeRecommend,userRecommend)
        responseMessage = "Recommendation added."
    except:
        responseMessage = "Recommendation was not added." + str(sys.exc_info()[0])
    
    return HttpResponse(responseMessage)

# Delete Request

# TODO format response
# RemoveRecipe?id=[val]
def RemoveRecipe(request):
    try:
        deleteRecipe = Recipe.objects.get(pk=request.GET["id"])
        responseMessage = deleteRecipe.name + " was deleted."
        # deleting the maps the recipe was associated with
        RecipeIngrMap.objects.filter(recipe__exact=deleteRecipe).delete()
        RecipeUserRecommendationsMap.objects.filter(recipe__exact=deleteRecipe).delete()
        deleteRecipe.delete()
    except:
        responseMessage = str(sys.exc_info()[0])

    return HttpResponse(responseMessage)
