from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    
    lesson = Lesson.objects.all()
    teacher = Teacher.objects.all()

    context = {
        "lesson" : lesson,
        "teacher" : teacher,
    }

    return render(request, "index_manytomany.html", context)