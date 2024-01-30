from django.urls import path
from todos.views import ShowTodoList, ShowTodoItem, create_todo_task, todo_list_update, delete_todo_list, create_todo_item

urlpatterns = [
    path("", ShowTodoList, name="todo_list_list"),
    path("<int:id>", ShowTodoItem, name="todo_list_detail"),
    path("create/", create_todo_task, name="todo_list_create"),
    path("<int:id>/edit/", todo_list_update, name="todo_list_update"),
    path("<int:id>/delete/", delete_todo_list, name="todo_list_delete"),
    path("items/create/", create_todo_item, name="todo_item_create"),
]
