from django.urls import path
from myuser.views import CheckLoginView
from myuser.views import SignupView
from myuser.views import LoginView
from myuser.views import LogoutView
app_name = 'myauth'
urlpatterns = [
   path('',CheckLoginView.as_view(),name='home'),
   path('check-login/',CheckLoginView.as_view(),name='check_login'),
   path('login/',LoginView.as_view(),name='login'),
   path('logout/',LogoutView.as_view(),name='logout'),
   path('signup/',SignupView.as_view(), name = 'signup'),
   path('forgot_password',CheckLoginView.as_view(),name='forgot_password'),
]


