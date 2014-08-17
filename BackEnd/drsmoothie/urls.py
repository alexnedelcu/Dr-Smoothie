from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'drsmoothie.rest.views.Ingredients', name='Ingredients'),
    # GET
    url(r'^IngredientsByNutrient$', 'drsmoothie.rest.views.IngredientsByNutrient', name='GetIngredientsByNutrient'),
    url(r'^Nutrients$', 'drsmoothie.rest.views.Nutrients', name='Nutrients'),
    url(r'^Ingredients$', 'drsmoothie.rest.views.Ingredients', name='Ingredients'),
    url(r'^RecipesByUser', 'drsmoothie.rest.views.RecipesByUser', name='RecipesByUser'),
    url(r'^FavoriteRecipes', 'drsmoothie.rest.views.FavoriteRecipes', name='FavoriteRecipes'),
    url(r'^TopRecipes', 'drsmoothie.rest.views.TopRecipes', name='TopRecipes'),
    # POST
    url(r'^AddRecipe', 'drsmoothie.rest.views.AddRecipe', name='AddRecipe'),
    url(r'^AddUser', 'drsmoothie.rest.views.AddUser', name='AddUser'),
    
    # url(r'^drsmoothie/', include('drsmoothie.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
