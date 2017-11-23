
angular.module('core').controller('HomeController', function($scope, $http, $location) {

   $scope.signIn = function() {
      $http({
         method: 'POST',
         url: 'http://127.0.0.1.xip.io:8000/users/signin/',
         data: {
            username: $scope.username,
            password: $scope.password
         }
      }).then(function() {
         $location.path('/myitems')
      }, function() {
         $scope.error = 'Invalid username or password.';
      });
   };
});
