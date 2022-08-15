from django.urls import path
from . import views

urlpatterns = [
    path('manytomany', views.index, name ="index_onetoone"),
]
