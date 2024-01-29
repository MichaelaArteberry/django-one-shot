from django.shortcuts import render, redirect
from todos.models import TodoList

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
