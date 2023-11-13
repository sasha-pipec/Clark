from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from models_app.models.abstract_time.models import AbstractTime
from .manager import CustomUserManager


class User(AbstractUser, AbstractTime):
    """Overriding the User model with the email field as primary"""

    username = models.CharField(max_length=150, blank=True, null=True, verbose_name='Имя')
    email = models.EmailField(_('email address'), unique=True)
    image = models.ImageField(upload_to='users/', verbose_name='Фото')
    confirmation_code = models.CharField(max_length=6, verbose_name='Код подтверждения')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'users'
        app_label = 'models_app'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
