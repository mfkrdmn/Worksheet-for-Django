from django.urls import path
from . import views

urlpatterns = [
    path('onetomany', views.index, name ="index"),
]
