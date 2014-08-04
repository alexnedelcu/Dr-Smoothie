'use strict';

/**
 * @ngdoc function
 * @name comdrsmoothieappApp.controller:AboutCtrl
 * @description
 * # AboutCtrl
 * Controller of the comdrsmoothieappApp
 */
angular.module('comdrsmoothieappApp')
  .controller('SmoothieListCtrl', function ($scope, $http) {
    $scope.smoothielist = [
    	{name :"Banana delight", recom : 10},
    	{name : "Strawberry delight", recom: 12},
		{name :"Banana delight", recom : 10},
    	{name : "Strawberry delight", recom: 12},
		{name :"Banana delight", recom : 10},
    	{name : "Strawberry delight", recom: 12}
    ];
  });
