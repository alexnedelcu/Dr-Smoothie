from django.http import HttpResponse
from models import *
from django.core import serializers
from django.utils import simplejson
# This is not necessary
#from django.views.decorators.csrf import csrf_protect
#from django.core.context_processors import csrf
import json
import sys
# Create your views here.

# GET Requests
def GetIngredient(request):
    retrievedIngredient = Ingredient.objects.get(pk=request.GET['id'])
    
    #Ingredient.objects.get(pk=request.GET['id'])
    return HttpResponse(serializers.serialize("json", [retrievedIngredient]))

def Ingredients(request):
    ingredients = Ingredient.objects.all()
    return HttpResponse(serializers.serialize("json", ingredients))

def Nutrients(request):
    nutrients = Nutrient.objects.all()
    return HttpResponse(serializers.serialize("json", nutrients))

def Users(request):
    users = User.objects.all()
    return HttpResponse(serializers.serialize("json", users))

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
    
    return HttpResponse(serializers.serialize("json", ingredients))
<<<<<<< HEAD
=======

def RecipesByUser(request):
    try:
        userfound = User.objects.get(pk=request.GET['key'])
    except User.DoesNotExist:
        userfound = None
    #if userfound is null:
    #    recipes = []
    #else:
    recipes = Recipe.objects.filter(user__exact = userfound)
    return HttpResponse(serializers.serialize("json", recipes))
    

def FavoriteRecipes(request):
    try:
        userfound = User.objects.get(pk=request.GET['key'])
    except:
        userfound = None
    
    favorites = RecipeUserRecommendationsMap.objects.filter(user__exact = userfound)
    
    return HttpResponse(serializers.serialize("json", favorites))

def TopRecipes(request):
    recipes = Recipe.objects.all()
    start = int(request.GET['start'])
    end = int(request.GET['end'])
    rlist = []

    for r in recipes:
        recommendations = len(RecipeUserRecommendationsMap.objects.filter(recipe=r))
        rlist.append((r, recommendations))

    list.sort(rlist, key= lambda tup: tup[1])
    return HttpResponse(serializers.serialize("json", rlist[start:end]))

def Search(request):

    return HttpResponse('')

# POST/PUT/UPDATE
def AddRecipe(request):
    data = json.loads(request.body)

    # retrieve needed data from data
    recipename = str(data["name"])
    ingredients = data["ingredients"]
    userkey = str(data["userkey"])

    # userfound should have a try statement
    userfound = User.objects.get(key=userkey)
    addedrecipe = Recipe.create(recipename, userfound)

    for ingr in ingredients:
        quantity = float(ingr["quantity"])
        ingrid = str(ingr["ingr_id"])
        ingrRetrieved = Ingredient.objects.get(pk=ingrid)
        rim = RecipeIngrMap.create(addedrecipe,ingrRetrieved,quantity)
    
    return HttpResponse('')

def AddUser(request):
    data = json.loads(request.body)
    try:
        newuserkey = str(data["userkey"])
        userexists = User.objects.get_or_create(key=newuserkey)
        responseMessage = 'User was created or already exists'
    except:
        responseMessage = 'User was not created.'

    return HttpResponse(responseMessage)

def RecommendRecipe(request):
    try:
        recipeRecommend = Recipe.objects.get(id=request.GET['recipeid'])
        userRecommend = Recipe.objects.get(userkey=request.GET['userkey'])

        createRecommendation = RecipeUserRecommendationsMap(recipe=recipeRecommend, user=userRecommend)
        createRecommendation.save()
        responseMessage = "Recommendation added."
    except:
        responseMessage = "Recommendation was not added."
    
    return HttpResponse(responseMessage)

# Delete Requests
def RemoveRecipe(request):
    try:
        deleteRecipe = Recipe.objects.get(pk=request.GET["id"])
        responseMessage = Recipe.name + " was deleted."
        # deleting the maps the recipe was associated with
        RecipeIngrMap.objects().filter(recipe__exact=deleteRecipe).delete()
        RecipeUserRecommendationsMap.objects().filter(recipe__exact=deleteRecipe).delete()
        deleteRecipe.delete()
    except:
        responseMessage = "Recipe was not deleted."

    return HttpResponse(responseMessage)
>>>>>>> FETCH_HEAD
