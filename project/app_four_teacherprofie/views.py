from django.shortcuts import render

# Create your views here.

def profile(request):
    return render(request, "teacher_profile.html")