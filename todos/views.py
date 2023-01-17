from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': 'todos/',
            'method': 'GET',
            'body': None,
            'description': 'Returns and array of todos'
        },
        {
            'Endpoint': 'todos/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single todo object'
        },
        {
            'Endpoint': 'todos/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new todo with data sent in post request'
        },
        {
            'Endpoint': 'todos/id/update/',
            'method': 'PUT',
            'body': {'body':""},
            'description': 'Updates an existing todo with data sent in post request'
        },
        {
            'Endpoint': 'todos/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes a todo object'
        },
    ]
    return Response(routes)