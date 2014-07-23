'use strict';

/**
 * @ngdoc overview
 * @name comdrsmoothieappApp
 * @description
 * # comdrsmoothieappApp
 *
 * Main module of the application.
 */
angular
  .module('comdrsmoothieappApp', [
    'ngAnimate',
    'ngCookies',
    'ngResource',
    'ngRoute',
    'ngSanitize',
    'ngTouch'
  ])
  .config(function ($routeProvider) {
    $routeProvider
      .when('/', {
        templateUrl: 'views/main.html',
        controller: 'MainCtrl'
      })
      .when('/smoothie', {
        templateUrl: 'views/smoothieList.html',
        controller: 'SmoothieListCtrl'
      })
      .otherwise({
        redirectTo: '/'
      });
  });
