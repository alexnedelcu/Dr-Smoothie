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
      .when('/smoothieListPersonal', {
        templateUrl: 'views/recipes.html',
        controller: 'MySmoothieListCtrl'
      })
      .when('/smoothieDetail', {
        templateUrl: 'views/smoothieDetail.html',
        controller: 'SmoothieDetailCtrl'
      })
      .when('/create', {
        templateUrl: 'views/createSmoothie.html',
        controller: 'CreateSmoothieCtrl'
      })
      .when('/search', {
        templateUrl: 'views/search.html',
        controller: 'SearchListCtrl'
      })
      .otherwise({
        templateUrl: 'views/main.html',
        controller: 'MainCtrl'
      });
  });

