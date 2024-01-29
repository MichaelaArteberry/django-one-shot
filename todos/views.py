from django.shortcuts import render, redirect
from todos.models import TodoList

# Create your views here.

def ShowTodoList(request):
  todo_list_list = TodoList.objects.all()
  context = {
    "todo_list_list": todo_list_list
  }

  return render(request, "todos/todos.html", context)
