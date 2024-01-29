from django.urls import path
from todos.views import ShowTodoList, ShowTodoItem

urlpatterns = [
    path("", ShowTodoList, name="todo_list_list"),
    path("todos/<int:id>", ShowTodoItem, name="todo_list_detail"),
]
