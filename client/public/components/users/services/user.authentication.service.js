
angular.module('users').factory('Authentication', function() {
   var user;

   return {
      setUser: function(u) {
         user = u;
      },
      getUser: function() {
         return user;
      }
   };
});
