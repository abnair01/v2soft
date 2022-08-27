from django import forms
from django.forms import Form
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.db.models import Q
from todo.models import TodoList
from django.utils.dateparse import parse_date

class TodoForm(Form):
    title = forms.CharField(max_length=100)
    due_date = forms.CharField()
    def clean_title(self):
        #import pdb;pdb.set_trace()
        return self.cleaned_data['title']
    def clean_due_date(self):
        #import pdb;pdb.set_trace()
        return parse_date(self.cleaned_data['due_date'])

class TodoItemForm(Form):
    todo_list_id = forms.CharField(max_length=100)
    item_title = forms.CharField(max_length=100)
    item_due_date = forms.CharField()

    def clean_todo_list_id(self):
        #import pdb;pdb.set_trace()
        return self.cleaned_data['todo_list_id']
    def clean_item_title(self):
        #import pdb;pdb.set_trace()
        return self.cleaned_data['item_title']
    def clean_item_due_date(self):
        #import pdb;pdb.set_trace()
        return parse_date(self.cleaned_data['item_due_date'])

"""
class TodoForm(Form):
    #Django uses BigAutoField for creating automatic pk.it is guaranteed to fit numbers from 1 to 9223372036854775807
    #PositiveBigIntegerField. Values from 0 to 9223372036854775807 are safe in all databases supported by Django.
    #Corresponding Field is PositiveIntegerField which has
    id = forms.PositiveBigIntegerField()
"""
