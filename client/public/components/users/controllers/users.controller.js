angular.module('users').controller('UsersController', function($scope, $location, User) {
   
   $scope.signUp = function() {
      var user = new User({
         first_name: $scope.first_name,
         last_name: $scope.last_name,
         username: $scope.username,
         password: $scope.password
      });

      user.$save().then(function() {
         $location.path('/');
      }, function() {
         $scope.error = 'That username is already in use.';
      });
   };
});
