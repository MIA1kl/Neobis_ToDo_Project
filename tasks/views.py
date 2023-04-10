from django.shortcuts import redirect, render
from django.views.generic import ListView,CreateView
from .models import TaskItem
from .forms import TaskItemCreateForm


class TodoItemListView(ListView):
    model = TaskItem
    template_name = 'tasks/todoitem_list.html'

class TodoItemCreateView(CreateView):
    model  = TaskItem
    template_name ='tasks/todoitemcreate_form.html'
    form_class  =TaskItemCreateForm
    success_url = '/todo/list'
