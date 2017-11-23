
angular.module('items').controller('ItemsController', function($scope, $http, Item) {
   // Item.query({
   //
   // }).$promise.then(function(items) {
   //    $scope.test = items;
   // });
   $http({
      method: 'GET',
      url: 'http://127.0.0.1.xip.io:8000/items/1'
   }).then(function(response) {
      $scope.test = response.data;
   });
});
