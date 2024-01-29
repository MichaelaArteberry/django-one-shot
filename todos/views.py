from django.shortcuts import render, redirect
from todos.models import TodoList
from todos.forms import TodoListForm

# Create your views here.

def ShowTodoList(request):
  todo_list_list = TodoList.objects.all()
  context = {
    "todo_list_list": todo_list_list
  }

  return render(request, "todos/todos.html", context)



def ShowTodoItem(request, id):
  todo_list_detail = TodoList.objects.get(id=id)
  context = {
    "todo_list_detail": todo_list_detail
  }
  return render(request, "todos/detail.html", context)


def create_todo_task(request):
    if request.method == "POST":
        form = TodoListForm(request.POST)
        if form.is_valid():
           list =form.save()
           return redirect("todo_list_detail", id=list.id)
    else:
     form = TodoListForm()

    context = {
    "form": form
  }

    return render(request, "todos/create.html", context)
