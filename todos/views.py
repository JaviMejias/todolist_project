from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TodoForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

@login_required
def todo_list(request):
    status = request.GET.get("status")
    todos = Todo.objects.filter(user=request.user)
    if status == "done":
        todos = todos.filter(is_done=True)
    elif status == "pending":
        todos = todos.filter(is_done=False)
    return render(request, "todos/todo_list.html", {"todos": todos})

@login_required
def todo_create(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect("todo_list")
    else:
        form = TodoForm()
    return render(request, "todos/todo_create.html", {"form": form})

@login_required
def todo_edit(request, pk):
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    
    is_completed = todo.is_done 
    
    if request.method == "POST":
        if is_completed:
            return redirect("todo_list")

        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect("todo_list")
    else:
        form = TodoForm(instance=todo)
        
    return render(request, "todos/todo_edit.html", {
        "form": form, 
        "todo": todo,
        "is_completed": is_completed
    })

@login_required
def todo_delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    if request.method == "POST":
        todo.delete()
        return redirect("todo_list")
    return render(request, "todos/todo_delete.html", {"todo": todo})

@login_required
def todo_toggle_done(request, pk):
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    todo.is_done = not todo.is_done
    todo.save()
    return JsonResponse({"success": True, "is_done": todo.is_done})
