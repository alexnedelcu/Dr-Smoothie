'use strict';

/**
 * @ngdoc function
 * @name comdrsmoothieappApp.factory.restFactory
 * @description
 * # restfactory
 * Controller of the comdrsmoothieappApp
 */
angular.module('comdrsmoothieappApp')
  .factory('restFactory', ['$http', function ($http) {

  var urlBase = 'http://localhost:8000';
  var restFactory = {};

  restFactory.getRecipeDetails = function(id){
  	return $http.get(urlBase + '/recipe' + id);
  };

  restFactory.getTopRecipes = function(){
  	return $http.get(urlBase + '/top/0/10');
  };

  restFactory.getMyRecipes = function(userId){
  	return $http.get(urlBase + '/myrecipes/' + userId);
  };

  restFactory.getMyFavorites = function(userId){
  	return $http.get(urlBase + '/myfavorites/' + userId);
  };

  restFactory.addRecipe = function(recipe){
  	return $http.post(urlBase + '/recipe', recipe);
  };

  restFactory.addUser = function(facebookID){
  	return $http.post(urlBase + '/AddUser', {fbID: facebookID}).success(function (data) {console.log(data)});
  };

  //delete doesnot take a body
  //we need to pass recipeid as well as userid
  restFactory.removeRecipe = function(recipe){
  	return $http.delete(urlBase + '/recipe/' + recipe.id);
  };

  restFactory.searchByName = function(name){
  	return $http.get(urlBase + '/search/' + name);
  };

  restFactory.searchByIngredient = function(ing){
  	return $http.get(urlBase + '/search/' + ing);
  };

  restFactory.searhByNutrient = function(nut){
  	return $http.get(urlBase + '/search/' + nut);
  };

  restFactory.getIngredients = function(type, successCallback){
    return $http.get(urlBase + '/Ingredients?type='+type).success(successCallback);
  };

  return restFactory;
  }]);
