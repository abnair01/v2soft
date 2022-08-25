from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.views import View
from todo.forms import TodoForm
from todo.forms import TodoItemForm
from todo.models import TodoList
from todo.models import TodoItem
# Create your views here.
from django.contrib.auth import get_user_model

from django.utils.dateparse import parse_date
class TodoView(View):
    form_class =  TodoForm
    template_name = 'todo.html'
    def get(self,request):
        form = self.form_class()
        user = get_user_model().objects.get(pk=request.user.id)
        todo_qs = TodoList.objects.filter(owner=user)
        context = {
            "todo_qs": todo_qs,
            "user": user.name,
            "form": form
        }
        return render(request,self.template_name,context)
    def post(self, request):
        context = {}
        form = self.form_class(request.POST)
        #import pdb; pdb.set_trace()
        if form.is_valid():
            user = get_user_model().objects.get(pk=request.user.id)
            #c_title = request.POST['title']
            #c_due_date = parse_date(request.POST['due_date'])
            c_title = form.cleaned_data['title']
            c_due_date = form.cleaned_data['due_date']
            new_todo = TodoList(owner=user,title=c_title,due_date=c_due_date)
            new_todo.save()
        return redirect("todo:todo")



class TodoItemView(View):
    form_class =  TodoItemForm
    template_name = 'todo.html'
    def post(self, request):
        context = {}
        form = self.form_class(request.POST)
        #import pdb; pdb.set_trace()
        if form.is_valid():
            user = get_user_model().objects.get(pk=request.user.id)
            #c_title = request.POST['title']
            #c_due_date = parse_date(request.POST['due_date'])
            c_todo = TodoList.objects.get(pk=form.cleaned_data['todo_list_id'])
            c_title = form.cleaned_data['item_title']
            c_due_date = form.cleaned_data['item_due_date']
            new_todo = TodoItem(todo=c_todo,title=c_title,due_date=c_due_date)
            new_todo.save()
        return redirect("todo:todo")

