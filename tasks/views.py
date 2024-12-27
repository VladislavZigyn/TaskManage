from django.shortcuts import render, redirect
from .models import *
from .forms import *

def home(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request,'base.html', context)

def tasks(request, c_id):
    category = Category.objects.get(pk=c_id)
    my_tasks = Tasks.objects.filter(category=category).filter(is_done=False)
    my_category = category.title
    context = {
        'tasks': my_tasks,
        'category': my_category
    }
    return render(request, 'tasks.html', context)

def description(request, task_id):
    task = Tasks.objects.get(pk=task_id)
    category_id = task.category.id
    context = {
        'task': task,
        'category_id': category_id
    }
    return render(request, 'description.html', context)

def task_del(request, task_id):
    task = Tasks.objects.get(pk=task_id)
    task.is_done = True
    task.save()
    category = task.category.id
    return redirect(tasks, c_id=category)

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(home)
    else:
        form = CategoryForm
        context = {
            'form': form
        }
        return render(request, 'add_category.html', context)

def add_task(request, category):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.category = Category.objects.get(title=category)
            post.save()
        return redirect(tasks, post.category.id)
    else:
        form = TaskForm
        context = {
            'form': form
        }
        return render(request, 'add_task.html', context)

def category_dell(request, c_id):
    category = Category.objects.get(pk=c_id)
    category.delete()
    return redirect(home)

def done_tasks(request):
    tasks = Tasks.objects.filter(is_done=True)
    context = {'tasks': tasks}
    return render(request, 'done_tasks.html', context)

def not_done(request, task_id):
    task = Tasks.objects.get(pk=task_id)
    task.is_done = False
    task.save()
    return redirect(done_tasks)

def done_tasks_dell(request):
    tasks = Tasks.objects.filter(is_done=True)
    tasks.delete()
    return redirect(home)