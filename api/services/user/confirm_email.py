from functools import lru_cache

from rest_framework.exceptions import ValidationError
from service_objects.services import ServiceWithResult
from django import forms

from models_app.models import User


class UserConfirmEmailService(ServiceWithResult):
    confirmation_code = forms.CharField()

    custom_validations = ["check_confirmation_code", ]

    def process(self):
        self.run_custom_validations()
        self.result = self._confirm_email
        return self

    @property
    def _confirm_email(self) -> User:
        user = self._user_get.last()
        user.confirmation_code = ''
        user.save()
        return user

    @property
    @lru_cache()
    def _user_get(self):
        return User.objects.filter(confirmation_code=self.cleaned_data['confirmation_code'])

    def check_confirmation_code(self):
        if not self._user_get.exists():
            raise ValidationError("Невенрный код подтверждения")
