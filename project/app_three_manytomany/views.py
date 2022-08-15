from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    
    lesson = Lesson.objects.all()
    picture = Teacher.objects.all()

    context = {
        "lesson" : lesson,
        "picture" : picture,
    }

    return render(request, "index_manytomany.html", context)