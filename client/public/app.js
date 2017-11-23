'use strict';

var retail = angular.module("retail", []);
var core = angular.module("core", []);
var users = angular.module("users", []);
var items = angular.module("items", []);

angular
   .module('SampleApplication', [
      'appRoutes',
      'retail',
      'core',
      'users',
      'items',
      'ngResource',
      'ngMaterial'
   ]);
