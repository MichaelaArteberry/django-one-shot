from django.urls import path
from todos.views import ShowTodoList

urlpatterns = [
    path("", ShowTodoList, name="todo_list_list"),
]
