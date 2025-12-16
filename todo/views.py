from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Task


@login_required
def home(request):
    if request.method == 'POST':
        Task.objects.create(
        user=request.user,
        title=request.POST.get('title')
    )
        return redirect('home')


    tasks = Task.objects.filter(user=request.user)
    return render(request, 'todo/home.html', {'tasks': tasks})


@login_required
def complete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = True
    task.save()
    return redirect('home')

@login_required
def delete_task(request, task_id):
    Task.objects.get(id=task_id).delete()
    return redirect('home')