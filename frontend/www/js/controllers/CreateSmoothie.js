'use strict';

/**
 * @ngdoc function
 * @name comdrsmoothieappApp.controller:AboutCtrl
 * @description
 * # AboutCtrl
 * Controller of the comdrsmoothieappApp
 */
angular.module('comdrsmoothieappApp')
  .controller('CreateSmoothieCtrl', ['$scope', 'restFactory', function ($scope, restFactory) {
    $scope.selectedIngredients = [];

    restFactory.getIngredients("vegetable", function (data) { $scope.vegetables = data; console.log($scope.vegetables); });
    restFactory.getIngredients("fruit", function (data) { $scope.fruits = data; });
    restFactory.getIngredients("nuts", function (data) { $scope.nuts = data; });
    restFactory.getIngredients("other", function (data) { $scope.others = data; });

    $scope.newSmoothieIngredientListClass = "hidden";

    function removeIngredientFromLists (ingredient) {
        var index_veg = $scope.vegetables.indexOf(ingredient);
        var index_fru = $scope.fruits.indexOf(ingredient);
        var index_nut = $scope.nuts.indexOf(ingredient);
        var index_oth = $scope.others.indexOf(ingredient);

        $scope.vegetables.splice(index_veg, 1);
        $scope.fruits.splice(index_fru, 1);
        $scope.nuts.splice(index_nut, 1);
        $scope.others.splice(index_oth, 1);
    }

    $scope.addIngredientToRecipe = function (ingredient) {

        // add ingredient to smoothie
        $scope.selectedIngredients.push(ingredient);

        // remove the ingredient from the available ingredient list
        removeIngredientFromLists(ingredient);

        // show the new smoothie ingredient list
        $scope.newSmoothieIngredientListClass = "";

    };

    $scope.removeIngredientFromRecipe = function (ingredient) {
        for (var i=0; i<$scope.selectedIngredients.length; i++) {
            console.log("index of element deleted: " + $scope.selectedIngredients.indexOf(ingredient));
            if ($scope.selectedIngredients[i].name == ingredient.name) {
                $scope.selectedIngredients.splice(i, 1);
                i--;
            }
        }

        // hide the new smoothie ingredient list if there are not ingredients added to it.
        if ($scope.selectedIngredients.length == 0)
            $scope.newSmoothieIngredientListClass = "hidden";
    };
  }]);
