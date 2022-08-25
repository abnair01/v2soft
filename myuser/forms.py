from django import forms
from django.forms import Form
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.db.models import Q
from myuser.utils import is_email
class CheckLoginForm(Form):
    login_id = forms.CharField(max_length=150)
    def clean_login_id(self):
        #checks the phone or email in the database as well
        data = self.cleaned_data['login_id']
        if not is_email(data):
            raise ValidationError(_('Invalid email'),code='invalid_email')
        else:
            try:
                user = get_user_model().objects.get(Q(email__exact=data))
            except get_user_model().DoesNotExist:
                user = None 
            except get_user_model().MultipleObjectsReturned:
                raise ValidationError(_('User email is not unique'), code = 'user_email_not_unique')
            
        return user

class SignupForm(ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['email','name','password']
        widgets = {'password': forms.PasswordInput}

class LoginForm(Form):
    login_id = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
    def clean_login_id(self):
        #checks the phone or email in the database as well
        data = self.cleaned_data['login_id']
        if not is_email(data):
            raise ValidationError(_('Invalid email'),code='invalid_email')
        else:
            try:
                user = get_user_model().objects.get(email=data)
                data = user.email
            except get_user_model().DoesNotExist:
                raise ValidationError(_('User email does not exists'), code = 'user_email_doesnot_exists')
            except get_user_model().MultipleObjectsReturned:
                raise ValidationError(_('User email is not unique'), code = 'user_email_not_unique')
        return data
