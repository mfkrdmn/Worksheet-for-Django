from django.shortcuts import render
from .models import *

# Create your views here.

def profile(request,pk):

    teachers = TeacherProfile.objects.filter(name=pk)

    context = {
        'teachers' : teachers
    }

    return render(request, "teacher_profile.html", context)


def lecture(request,pk):

    lectures = Lecture.objects.filter(name=pk)

    context = {
        'lectures' : lectures
    }

    return render(request, "lecturepage.html", context)
