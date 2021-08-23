from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def index(request):
    tasks = Task.objects.order_by('id')
    context = {'title': 'Main Page', 'tasks': tasks}
    return render(request, 'main/index.html', context)


def about(request):
    return render(request, 'main/about.html')


def create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            err = 'Form is not valid'
    form = TaskForm()
    context = {
        'form': form,
        'err': err,
    }
    return render(request, 'main/create.html', context)
