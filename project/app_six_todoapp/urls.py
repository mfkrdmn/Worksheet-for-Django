from django.urls import path
from . import views

urlpatterns = [
    path('todoapp', views.todo, name ="todo"),
]
