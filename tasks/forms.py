from django import forms
from .models import TaskItem


class TaskItemCreateForm(forms.ModelForm):
    class Meta:
        model = TaskItem
        fields =('title', 'body','due_date','category')