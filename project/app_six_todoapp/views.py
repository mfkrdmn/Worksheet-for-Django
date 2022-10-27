from asyncio import tasks
from multiprocessing import context
from django.shortcuts import render, redirect
from .models import *
from .forms import *
# Create your views here.

def todo(request):

    tasks = Task.objects.all()

    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/todoapp")

    context = {
        "tasks" : tasks,
        'form' : form,
    }

    return render(request, 'todo.html', context)


def deleteTask(request,pk):

    item = Task.objects.filter(id=pk)

    item.delete()
    return redirect("/todoapp")
