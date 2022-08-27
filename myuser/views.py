from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.views import View
from myuser.forms import CheckLoginForm
from myuser.forms import SignupForm
from myuser.forms import LoginForm
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# Create your views here.
class CheckLoginView(View):
    form_class =  CheckLoginForm
    template_name = 'check_login.html'
    signup_template = 'signup.html'
    login_template = 'login.html'
    def get(self,request):
        form = self.form_class()
        return render(request,self.template_name,{'form':form})
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.cleaned_data['login_id']
            if(user is None):
                return render(request,self.signup_template,{'form':form})
            else:
                return render(request,self.login_template,{'form':form})
        return render(request,self.template_name,{'form':form})

class SignupView(View):
    form_class =  SignupForm
    template_name = 'signup.html'
    next_template = 'check_login.html'
    def get(self,request):
        form = self.form_class()
        return render(request,self.template_name,{'form':form})
    def post(self, request):
        context = {}
        form = self.form_class(request.POST)
        if form.is_valid():
            #get model object
            #new_user=form.save(commit=False)
            #cleaned(normalized) data
            email=form.cleaned_data['email']
            name=form.cleaned_data['name']
            password=form.cleaned_data['password']
            #create a new user object
            new_user = get_user_model()(
                email=email,
                name=name,
                password=password
            )
            #call set password so that password is stored as hash
            new_user.set_password(password)
            new_user.save()
            return render(request, self.next_template,{'form':form})
        return render(request,self.template_name,{'form':form})


@method_decorator(csrf_exempt, name='dispatch')
class LoginView(View):
    form_class =  LoginForm
    template_name = 'login.html'
    def get(self,request):
        form = self.form_class()
        return render(request,self.template_name,{'form':form})
    def post(self, request):
        #Todo if user is already logged in, then logout, delete session and ask to login again
        context = {}
        form = self.form_class(request.POST)
        if(form.is_valid()):
            username = form.cleaned_data['login_id']
            password = form.cleaned_data['password']

            user = authenticate(request,username=username,password=password)
            if user is not None:
                logout(request)
                login(request,user)
                #below code may need to be removed.
                #this is handled in user logged in
                #signal handler
                """
                UserSession.objects.get_or_create(
                    user = user,
                    session_id = request.session.session_key
                )
                """
                #return HttpResponse("Logged In")
                return redirect(reverse('todo:todo'))
            else:
                return render(request, self.template_name,{'form':form})

        return render(request,self.template_name,{'form':form})


@method_decorator(login_required(login_url='myauth:check_login'),name='dispatch')
class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect(reverse('myauth:check_login'))
