from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.views import View
from todo.forms import TodoForm
from todo.forms import TodoItemForm
from todo.forms import UpdateTodoForm
from todo.forms import UpdateTodoItemForm
#from todo.forms import DeleteTodoItemForm
from todo.models import TodoList
from todo.models import TodoItem
from django.contrib.auth import get_user_model
import json
from django.utils.decorators import method_decorator
from django.utils.dateparse import parse_date
from django.contrib.auth.decorators import login_required

@method_decorator(login_required(login_url='myauth:check_login'),name='dispatch')
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



@method_decorator(login_required(login_url='myauth:check_login'),name='dispatch')
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



@method_decorator(login_required(login_url='myauth:check_login'),name='dispatch')
class UpdateTodoView(View):
    form_class =  UpdateTodoForm
    template_name = 'todo.html'
    def post(self, request):
        context = {}
        form = self.form_class(request.POST)
        #import pdb; pdb.set_trace()
        if form.is_valid():
            #user = get_user_model().objects.get(pk=request.user.id)
            #c_title = request.POST['title']
            #c_due_date = parse_date(request.POST['due_date'])
            todo = TodoList.objects.get(pk=form.cleaned_data['todo_id'])
            todo.title = form.cleaned_data['title']
            #todo.due_date = form.cleaned_data['due_date']
            todo.save()
        return redirect("todo:todo")

@method_decorator(login_required(login_url='myauth:check_login'),name='dispatch')
class UpdateTodoItemView(View):
    form_class =  UpdateTodoItemForm
    template_name = 'todo.html'
    def post(self, request):
        context = {}
        form = self.form_class(request.POST)
        #import pdb; pdb.set_trace()
        if form.is_valid():
            #user = get_user_model().objects.get(pk=request.user.id)
            #c_title = request.POST['title']
            #c_due_date = parse_date(request.POST['due_date'])
            todo_item = TodoItem.objects.get(pk=form.cleaned_data['item_id'])
            todo_item.title = form.cleaned_data['item_title']
            todo_item.due_date = form.cleaned_data['item_due_date']
            todo_item.save()
        return redirect("todo:todo")

@method_decorator(login_required(login_url='myauth:check_login'),name='dispatch')
class DeleteTodoItemView(View):
    def post(self, request):
        json_data=json.loads(request.body)
        #import pdb; pdb.set_trace()
        #response_data={'status':'failed'}
        #form = DeleteTodoItemForm(json_data)
        item_ids = []
        for obj in json_data['items']:
            item_ids.append(obj['itemid'])
        #This will do bulk delete
        if(len(item_ids) > 0):
            todo_item_qs = TodoItem.objects.filter(id__in=item_ids)
            todo_item_qs.delete()
            return HttpResponse("Todo Items deleted")
        else:
            return HttpResponse("Empty data")

