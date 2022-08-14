from multiprocessing import context
import re
from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):

    lesson = Lesson.objects.all()

    context = {
        "lesson" : lesson
    }

    return render(request, "index.html", context)