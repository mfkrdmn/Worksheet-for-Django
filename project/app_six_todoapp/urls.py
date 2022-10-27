from django.urls import path
from . import views

urlpatterns = [
    path('todoapp', views.todo, name ="todo"),
    path('delete/<str:pk>/', views.deleteTask, name ="deleteTask"),
]
