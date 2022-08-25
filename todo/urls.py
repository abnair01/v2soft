from django.urls import path
from todo.views import TodoView
from todo.views import TodoItemView
#from myuser.views import SignupView
#from myuser.views import LoginView
app_name = 'todo'
urlpatterns = [
   #path('',CheckLoginView.as_view(),name='home'),
   path('todo/',TodoView.as_view(),name='todo'),
   path('todo_item/',TodoItemView.as_view(),name='todo_item'),
   #path('login/',LoginView.as_view(),name='login'),
   #path('signup/',SignupView.as_view(), name = 'signup'),
   #path('forgot_password',CheckLoginView.as_view(),name='forgot_password'),
]


