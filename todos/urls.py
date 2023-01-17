from django.urls import path 
from . import views

urlpatterns = [ 
    path('', views.getRoutes),
    path('todos/', views.getTodos),
    path('todos/create', views.createTodo),
    path('todos/<str:pk>/', views.getTodo),
]