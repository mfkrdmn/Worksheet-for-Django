from django.urls import path
from . import views

urlpatterns = [
    path('profile/<str:pk>', views.index, name ="index_onetoone"),
]
