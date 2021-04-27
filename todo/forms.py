from django.forms import ModelForm
from .models import Task

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['id', 'task_name', 'task_desc', 'task_deadline']

        labels = {
            'id' : "Task ID",
            'task_name' : 'Task Name',
            'task_desc' : 'Task Description',
            'task_deadline' : 'Task Deadline',
        }