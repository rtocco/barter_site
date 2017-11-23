angular.module('users').factory('User', function($resource) {
      return $resource(
         'http://127.0.0.1.xip.io:8000/users/:id',
         {id:'@id'},
         {
            save: {
               url: 'http://127.0.0.1.xip.io:8000/users/ ',
               method: 'POST',
               isArray: false
            }
         }
      );
   });
