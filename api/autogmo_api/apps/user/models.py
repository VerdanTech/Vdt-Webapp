from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import UserManager

class User(AbstractBaseUser):
    """
    Class to handle user authentication and characteristics
    """

    email = models.EmailField(_("email address"), unique=True)
    username = models.CharField(_("username"), max_length=50)
    created_at = models.DateTimeField(_("date of creation"), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
