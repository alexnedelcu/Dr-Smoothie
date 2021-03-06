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

# GET Requests
def GetIngredient(request):
    retrievedIngredient = Ingredient.objects.get(pk=request.GET['id'])
    
    #Ingredient.objects.get(pk=request.GET['id'])
    return HttpResponse(ConvertIngredientsToJson([retrievedIngredient]))

# /Ingredients
def Ingredients(request):
    if "type" in request.GET:
        arg = str(request.GET["type"])
        try:
            ingredientType = IngredientType.objects.get(type=arg)
            ingredients = Ingredient.objects.filter(type__exact = ingredientType)
        except:
            ingredients = []
    else:
        ingredients = Ingredient.objects.all()

    jsonlist = ConvertIngredientsToJson(ingredients)
    
    return HttpResponse(jsonlist)

# /Nutrients
def Nutrients(request):
    nutrients = Nutrient.objects.all()
    #djangojson = serializers.serialize("json", nutrients)
    jsonlist = ConvertNutrListToJsonList(nutrients)

    return HttpResponse(jsonlist)

# /IngredientByRecipe?id=[value]
def IngredientsByRecipe(request):
    recipeid = str(request.GET["id"])
    ingrlist = []
    try:
        recipe = Recipe.objects.get(pk=recipeid)
        recipemappings = RecipeIngrMap.objects.filter(recipe__exact=recipe)
        for rm in recipemappings:
            ingrlist.append(rm.ingredient)
    except:
        ingrlist = []
    return HttpResponse(ConvertIngredientsToJson(ingrlist))

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
    jsonlist = ConvertIngredientsToJson(ingredients)
    return HttpResponse(jsonlist)

# TODO json formatting
# /RecipesByUser?userkey=[sample userkey]
def RecipesByUser(request):
    try:
        userfound = User.objects.get(key=request.GET['userkey'])
        recipes = Recipe.objects.filter(user__exact = userfound)
        
        reclist = CreateRecommendationCountList(recipes)
        jsonlist = ConvertRecipeToJsonList(recipes, reclist)
        
        return HttpResponse(jsonlist)

    except User.DoesNotExist:
        recipes = []
        return HttpResponse(serializers.serialize("json", []))
    
# TODO json formatting
# /FavoriteRecipes
def FavoriteRecipes(request):
    try:
        userfound = User.objects.get(key=request.GET['userkey'])
        favorites = RecipeUserRecommendationsMap.objects.filter(user__exact=userfound)
        
        recipes = []
        recslist = []
        for rmap in favorites:
            recipes.append(rmap.recipe)
            reccount = RecipeUserRecommendationsMap.objects.filter(recipe__exact=rmap.recipe).count()
            recslist.add(reccount)

        jsonlist = ConvertRecipeToJsonList(recipes, reclist)

        return HttpResponse(jsonlist)

    except:
        return HttpResponse(serializers.serialize("json", []))

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

    sorted(rlist, key=lambda x: x[1])

    recipes = []
    recs = []
    for pair in rlist:
        recipes.append(pair[0])
        recs.append(pair[1])

    jsonlist = ConvertRecipeToJsonList(recipes, recs)
    return HttpResponse(jsonlist)

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
        
        reclist = CreateRecommendationCountList(recipes)
        jsonlist = ConvertModelToJsonList(recipes, reclist)
        return HttpResponse(jsonlist)


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

        reclist = CreateRecommendationCountList(recipes)
        jsonlist = ConvertModelToJsonList(recipes, reclist)
        return HttpResponse(jsonlist)

# TODO not even started
# /Search/Recipe?name=[str]
def SearchRecipe(request):
    recipename = str(request.GET['name'])
    recipefound = Recipe.objects.all()

    recipes = []
    for r in recipefound:
        if recipename.lower() in str(r.name).lower():
            recipes.append(r)

    reclist = CreateRecommendationCountList(recipes)
    jsonlist = ConvertModelToJsonList(recipes, reclist)
    return HttpResponse(jsonlist)

# POST/PUT/UPDATE
# /AddRecipe
# request.body = (SampleRequestData.json)
def AddRecipe(request):
    recipename = str(request.GET['name'])
    ingrname = str(request.GET['ingr'])
    rec = 0
    Recipe.create(recipename, "Brian")
    # if request.method == "OPTIONS":
    #     methods = ['get', 'post', 'put', 'delete', 'options']
    #     optionsResponse = HttpResponse()
    #     optionsResponse['allow'] = ','.join(methods)
    #     return optionsResponse

    # data = json.loads(request.body)

    # # retrieve needed data from data
    # recipename = str(data["name"])
    # ingredients = data["ingredients"]
    # userkey = str(data["userkey"])

    # # userfound should have a try statement
    # try:
    #     userfound = User.objects.get(key=userkey)
    # except:
    #     userfound = None
    # if userfound is not None:
    #     try:
    #         addedrecipe = Recipe.create(recipename, userfound)
    #     except:
    #         return HttpResponse('already exists')
    #     for ingr in ingredients:
    #         quantity = float(ingr["quantity"])
    #         ingrid = str(ingr["ingr_id"])
    #         ingrRetrieved = Ingredient.objects.get(pk=ingrid)
    #         rim = RecipeIngrMap.create(addedrecipe,ingrRetrieved,quantity)

    return HttpResponse('')

# TODO: handle exceptions and null user
# format response
# /AddUser
# request.body = (SampleRequestData.json)
def AddUser(request):
    data = json.loads(request.body)
    try:
        newuserkey = str(data["userkey"])
        user, exists = User.objects.get_or_create(key=newuserkey)
        if not exists:
            responseMessage = user.key + " already exists."
        else:    
            responseMessage = '{userKey: "' + user.key + '"}'
    except:
        responseMessage = '{error: "User was not created."}'

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



# view used only for Facebook redirect after successful share or login
def RedirectURL(request) :
    return HttpResponse('<html><body><script>window.close();</script></body></html>')
