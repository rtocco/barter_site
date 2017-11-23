angular
   .module('appRoutes', ["ui.router"])
   .config(['$stateProvider', '$urlRouterProvider', function($stateProvider, $urlRouterProvider) {

      // $stateProvider.state({
      //    name: 'retail',
      //    url: '/',
      //    templateUrl: 'public/components/retail/templates/retail.template.html',
      //    controller: 'RetailController'
      // });
      $stateProvider.state({
         name: 'home',
         url: '/',
         templateUrl: 'public/components/core/templates/home.template.html',
         controller: 'HomeController'
      })
      .state({
         name: 'signup',
         url: '/signup',
         templateUrl: 'public/components/users/templates/signup.template.html',
         controller: 'UsersController'
      })
      .state({
         name: 'myitems',
         url: '/myitems',
         templateUrl: 'public/components/items/templates/my-items.template.html',
         controller: 'ItemsController'
      });

      $urlRouterProvider.otherwise('/');
   }]);
