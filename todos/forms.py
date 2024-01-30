from django.forms import ModelForm
from todos.models import TodoList, TodoItem


class TodoListForm(ModelForm):
    class Meta:
        model = TodoList
        fields = (
            "name",
        )



class TodoListUpdate(ModelForm):
    class Meta:
        model = TodoList
        fields = (
            "name",
        )




class add_todo_item(ModelForm):
    class Meta:
        model = TodoItem
        fields = (
            "task",
            "due_date",
            "is_completed",
            "list",
        )




class update_item(ModelForm):
    class Meta:
        model = TodoItem
        fields = (
            "task",
            "due_date",
            "is_completed",
            "list",
        )
