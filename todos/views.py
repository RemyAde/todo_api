from django.http import JsonResponse


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
    return JsonResponse(routes, safe=False)