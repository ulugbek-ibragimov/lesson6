from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from .managers import UserManager

class User(AbstractUser):
    first_name = None
    last_name = None
    email = None
    login = models.CharField(
        _('Login'),
        max_length=100,
        unique=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ))
    USERNAME_FIELD = "login"
    REQUIRED_FIELDS = []
    objects = UserManager()
