from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoCreationForm

def home_page(request):
    context = {
        'text':'Just poking around things!!',
    }
    return render(request,'todo/home.html', context)

def todo_list(request):
    todos = Todo.objects.all()
    context = {
        'todo_list': todos
    }
    return render(request, 'todo/list.html', context)

def todo_detail(request, id):
    todo = Todo.objects.get(id=id)
    context = {
        'todo': todo
    }
    return render(request, 'todo/detail.html', context)

def todo_create(request):
    form = TodoCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('todos:list')
    context = {
        'form': form,
    }
    return render(request, 'todo/create.html', context)

def todo_update(request, id):
    todo = Todo.objects.get(id=id)
    form = TodoCreationForm(request.POST or None, instance=todo)
    if form.is_valid():
        form.save()
        return redirect('todos:list')
    context = {
        'form': form,
    }
    return render(request, 'todo/update.html', context)

def todo_delete(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect('todos:home')
