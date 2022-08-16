from django.urls import path
from . import views

urlpatterns = [
    path('profile/<str:pk>', views.profile, name ="index_profile"),
    path('lecture/<str:pk>', views.lecture, name ="index_lecture"),
]
