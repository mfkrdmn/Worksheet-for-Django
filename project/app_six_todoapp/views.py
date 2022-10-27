from asyncio import tasks
from multiprocessing import context
from django.shortcuts import render
from .models import *
# Create your views here.

def todo(request):

    tasks = Task.objects.all()

    context = {
        "tasks" : tasks
    }

    return render(request, 'todo.html', context)