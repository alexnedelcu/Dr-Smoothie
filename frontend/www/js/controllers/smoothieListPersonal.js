'use strict';

/**
 * @ngdoc function
 * @name comdrsmoothieappApp.controller:MySmoothieListCtrl
 * @description
 * # MySmoothieListCtrl
 * Controller of the comdrsmoothieappApp
 */
angular.module('comdrsmoothieappApp')
  .controller('MySmoothieListCtrl', ['$scope', 'restFactory', function ($scope, restFactory) {
    
    $scope.mySmoothies = [
        {name:'Hearty Fruit and Oat Smoothie', recommendations: 30},
        {name:'Mango and Yogurt Smoothie', recommendations: 20},
        {name:'Green Ginger-Peach Smoothie', recommendations: 30}
    ];

    $scope.showSmoothieDetails = function(id) {
      window.location = '#/smoothieDetail';
    };
  }]);
