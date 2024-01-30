from django.shortcuts import render, redirect, get_object_or_404
from todos.models import TodoList
from todos.forms import TodoListForm, TodoListUpdate, add_todo_item, update_item

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







def todo_list_update(request, id):
    list = get_object_or_404(TodoList, id=id)
    if request.method == "POST":
        form = TodoListUpdate(request.POST, instance=list)
        if form.is_valid():
            list = form.save()
            return redirect("todo_list_detail", id=id)
    else:
        form = TodoListUpdate()

    context = {
        "form": form,
        "todolist": list,
    }

    return render(request, "todos/edit.html", context)





def delete_todo_list(request, id):
  model_instance = TodoList.objects.get(id=id)
  if request.method == "POST":
    model_instance.delete()
    return redirect("todo_list_list")

  return render(request, "todos/delete.html")





def create_todo_item(request):
    list = TodoList.objects.all()
    if request.method == "POST":
        form = add_todo_item(request.POST)
        if form.is_valid():
           item =form.save()
           return redirect("todo_list_detail", id=item.list.id)
    else:
     form = add_todo_item()

    context = {
    "form": form,
    "list_of_lists": list,
  }

    return render(request, "todos/items/create.html", context)




def TodoItemUpdate(request, id):
  list = TodoList.objects.all()
  if request.method == "POST":
    form = update_item(request.POST)
    if form.is_valid():
      item = form.save()
      return redirect("todo_list_detail", id=item.list.id)

  else:
    form = update_item()

  context = {
    "form": form,
    "list_of_lists": list,
  }

  return render(request, "todos/items/edit.html", context)
