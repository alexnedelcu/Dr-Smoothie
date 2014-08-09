'use strict';

/**
 * @ngdoc function
 * @name comdrsmoothieappApp.controller:MySmoothieListCtrl
 * @description
 * # MySmoothieListCtrl
 * Controller of the comdrsmoothieappApp
 */
angular.module('comdrsmoothieappApp')
  .controller('TopSmoothieListCtrl', function ($scope) {
    $scope.awesomeThings = [
      'HTML5 Boilerplate',
      'AngularJS',
      'Karma'
    ];
    $scope.topSmoothies = [
        {name:"Hearty Fruit and Oat Smoothie", recommendations: 30},
        {name:"Mango and Yogurt Smoothie", recommendations: 20},
        {name:"Green Ginger-Peach Smoothie", recommendations: 30},
        {name:"Tropical Blueberry Smoothie", recommendations: 30},
        {name:"Oatmeal Smoothie", recommendations: 30},
        {name:"Strawberry, Mango, Yogurt Smoothie", recommendations: 30},
        {name:"Fruit Smoothie", recommendations: 30},
        {name:"Yogurt-Pistachio Smoothie", recommendations: 30},
        {name:"Winter Smoothie", recommendations: 30},
        {name:"Avocado-Pear Smoothie", recommendations: 30},
        {name:"Green Ginger-Peach Smoothie", recommendations: 30},
        {name:"Tropical Blueberry Smoothie", recommendations: 30},
        {name:"Oatmeal Smoothie", recommendations: 30},
        {name:"Strawberry, Mango, Yogurt Smoothie", recommendations: 30},
        {name:"Fruit Smoothie", recommendations: 30},
        {name:"Yogurt-Pistachio Smoothie", recommendations: 30},
        {name:"Winter Smoothie", recommendations: 30}
    ];
    $scope.showSmoothieDetails = function(id) {
      window.location = '#/smoothieDetail';
    };
  });
