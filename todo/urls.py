from django.urls import path
from todo.views import TodoView
from todo.views import TodoItemView
from todo.views import UpdateTodoView
from todo.views import UpdateTodoItemView
from todo.views import DeleteTodoItemView
#from myuser.views import SignupView
#from myuser.views import LoginView
app_name = 'todo'
urlpatterns = [
   path('todo/',TodoView.as_view(),name='todo'),
   path('todo_item/',TodoItemView.as_view(),name='todo_item'),
   path('update_todo/',UpdateTodoView.as_view(),name='update_todo'),
   path('update_todo_item/',UpdateTodoItemView.as_view(),name='update_todo_item'),
   path('delete_todo_item/',DeleteTodoItemView.as_view(),name='delete_todo_item'),
]


