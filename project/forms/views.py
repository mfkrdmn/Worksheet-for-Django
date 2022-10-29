from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth.models import User
# Create your views here.

def forms(request): #with forms

    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/forms")

    context = {
        "form" : form
    }

    return render(request, "forms.html", context)

def register(request): #without forms

    if request.method == "POST":
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
    
    else:
        return render(request, 'register.html')

    
