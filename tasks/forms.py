from django import forms
from .models import TaskItem

class TaskItemUpdateForm(forms.ModelForm):
    class Meta:
        model = TaskItem
        fields =('title','body','due_date','task_finished','category')

class TaskItemCreateForm(forms.ModelForm):
    class Meta:
        model = TaskItem
        fields =('title', 'body','due_date','category')