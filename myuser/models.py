from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import(
    BaseUserManager, AbstractBaseUser
)
class TimeStamp(models.Model):
    created_on = models.DateTimeField(auto_now_add = True)
    updated_on = models.DateTimeField(auto_now = True)
    
    class Meta:
        abstract = True
class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        user = self.model(email=self.normalize_email(email),phone=phone)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(email, password=password)
        user.is_admin = True
        user.save(using=self._db)


class MyUser(AbstractBaseUser,TimeStamp):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=50)
    REQUIRED_FIELDS = ['name']
    USERNAME_FIELD = 'email'
    objects = MyUserManager()
    def get_short_name(self):
        return self.email

    def get_full_name(self):
        return self.email

    def __str__(self):
        return self.email
