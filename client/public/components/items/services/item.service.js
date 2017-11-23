angular.module('items').factory('Item', function($resource) {
   return $resource(
      'http://127.0.0.1.xip.io:8000/items/:id',
      {id:'@id'},
      {
         save: {
            url: 'http://127.0.0.1.xip.io:8000/items/ ',
            method: 'POST',
            isArray: false
         }
      }
   );
});
