'use strict';

/**
 * @ngdoc function
 * @name comdrsmoothieappApp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the comdrsmoothieappApp
 */
angular.module('comdrsmoothieappApp')
  .controller('MainCtrl', ['$scope', 'restFactory', function ($scope, restFactory) {
    $scope.awesomeThings = [
      'HTML5 Boilerplate',
      'AngularJS',
      'Karma'
    ];
  }]);
