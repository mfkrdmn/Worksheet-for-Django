from django.urls import path
from . import views

urlpatterns = [
    path('onetoone', views.index, name ="index_onetoone"),
]
