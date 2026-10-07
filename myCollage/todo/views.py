from django.urls import reverse
from . models import Task
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone


def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'todo/task_list.html', {'tasks': tasks})


def task_create(request):
    today = timezone.localdate()
    task_end_date = today + timezone.timedelta(days=7)
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        task_start_date = request.POST.get('task_start_date')
        task_end_date = request.POST.get('task_end_date')
        Task.objects.create(title=title, description=description, task_start_date=task_start_date, task_end_date=task_end_date)
        return redirect(reverse('todo:task_list'))
    return render(request, 'todo/task_form.html', {'today': today, 'task_end_date': task_end_date})


def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        today = request.POST.get('task_start_date')
        task_end_date = request.POST.get('task_end_date')
        task.completed = 'completed' in request.POST
        task.save()
        return redirect(reverse('todo:task_list'))
    return render(request, 'todo/task_form.html', {'task': task})



def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect(reverse('todo:task_list'))
    return render(request, 'todo/task_confirm_delete.html', {'task': task})


def task_toggle(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.completed = not task.completed
    task.save()
    return redirect(reverse('todo:task_list'))