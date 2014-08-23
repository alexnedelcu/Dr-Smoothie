from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'drsmoothie.rest.views.Ingredients', name='Ingredients'),
    
    # GET
    url(r'^IngredientsByNutrient$', 'drsmoothie.rest.views.IngredientsByNutrient', name='GetIngredientsByNutrient'),
    url(r'^GetIngredient$', 'drsmoothie.rest.views.GetIngredient', name='GetIngredient'),
    url(r'^Ingredients$', 'drsmoothie.rest.views.Ingredients', name='Ingredients'),
    url(r'^IngredientsByRecipe$', 'drsmoothie.rest.views.IngredientsByRecipe', name='IngredientsByRecipe'),
    url(r'^Nutrients$', 'drsmoothie.rest.views.Nutrients', name='Nutrients'),
    url(r'^GetRecipe$', 'drsmoothie.rest.views.GetRecipe', name='GetRecipe'),
    url(r'^RecipesByUser$', 'drsmoothie.rest.views.RecipesByUser', name='RecipesByUser'),
    url(r'^FavoriteRecipes$', 'drsmoothie.rest.views.FavoriteRecipes', name='FavoriteRecipes'),
    url(r'^TopRecipes$', 'drsmoothie.rest.views.TopRecipes', name='TopRecipes'),
    url(r'^Users$', 'drsmoothie.rest.views.Users', name='Users'),
    url(r'^Search/Recipe$', 'drsmoothie.rest.views.SearchRecipe', name='Search'),
    url(r'^Search/Ingredient$', 'drsmoothie.rest.views.SearchByIngredient', name='SearchIngr'),
    url(r'^Search/Nutrient$', 'drsmoothie.rest.views.SearchByNutrient', name='SearchByNutri'),
    
    # POST
    url(r'^AddRecipe', 'drsmoothie.rest.views.AddRecipe', name='AddRecipe'),
    url(r'^AddUser', 'drsmoothie.rest.views.AddUser', name='AddUser'),
    url(r'^RecommendRecipe', 'drsmoothie.rest.views.RecommendRecipe', name='RecommendRecipe'),
    
    # DELETE
    url(r'^RemoveRecipe', 'drsmoothie.rest.views.RemoveRecipe', name='RemoveRecipe'),
    
    # url(r'^drsmoothie/', include('drsmoothie.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
