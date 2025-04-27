from django.shortcuts import render, redirect, get_object_or_404
from .forms import TaskForm
from .models import Task

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    
    return render(request, 'create_task.html', {'form': form})

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})

def change_status(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    
    if request.method == 'POST':
        status = request.POST.get('status')
        task.status = status
        task.save()
    
    return redirect('task_list')