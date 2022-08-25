from django.db import models
from django.conf import settings
from myuser.models import TimeStamp
from django.utils.translation import gettext_lazy as _
# Create your models here.

class TodoList(TimeStamp, models.Model):
    class CompletionStatus(models.TextChoices):
        CREATED = 'CREATED', _('Created')
        IN_PROGRESS = 'IN_PROGRESS', _('In Progress')
        CLOSED = 'CLOSED', _('Closed')
    
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete = models.CASCADE
    )

    title = models.CharField(max_length=100)
    
    due_date = models.DateTimeField(
        blank = True,
        null = True,
        help_text = f'Date of Birth'
    )

    done = models.BooleanField(default=False)

class TodoItem(TimeStamp, models.Model):
    class ProgressStatus(models.TextChoices):
        CREATED = 'CREATED', _('Created')
        IN_PROGRESS = 'IN_PROGRESS', _('In Progress')
        CLOSED = 'CLOSED', _('Closed')
    
    todo = models.ForeignKey(
        TodoList, 
        on_delete = models.CASCADE
    )

    title = models.CharField(max_length=100)
    
    due_date = models.DateTimeField(
        blank = True,
        null = True,
        help_text = f'Date of Birth'
    )

    done = models.BooleanField(default=False)

    progress_status = models.CharField(
        max_length = 20,
        choices = ProgressStatus.choices,
        default = ProgressStatus.CREATED
    )
