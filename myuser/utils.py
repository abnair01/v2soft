from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core.validators import validate_email

def is_email(email):
    status = False
    try:
        validate_email(email)
        status = True
    except ValidationError:
        status = False
    return status

