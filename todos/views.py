from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TodoSerializer
from .models import Todo


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


@api_view(['GET'])
def getTodos(request):
    todos = Todo.objects.all()
    serializer = TodoSerializer(todos, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getTodo(request, pk):
    todo = Todo.objects.get(id=pk)
    serializer = TodoSerializer(todo, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def createTodo(request):
    data = request.data

    todo = Todo.objects.create(
        body = data['body']
    )
    serializer = TodoSerializer(todo, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
def updateTodo(request, pk):
    data = request.data
    todo = Todo.objects.get(id=pk)
    serializer = TodoSerializer(todo, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def deleteTodo(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return Response("Todo was deleted")