from rest_framework.exceptions import ValidationError
from service_objects.services import ServiceWithResult
from django import forms

from clark_app.utils import confirm_registration
from models_app.models import User


class UserCreateService(ServiceWithResult):
    email = forms.EmailField()
    password = forms.CharField()

    custom_validations = ["password_confirm", "user_presence", ]

    def process(self):
        self.run_custom_validations()
        self.result = self._user_create
        return self

    @property
    def _user_create(self):
        user = User.objects.create_user(
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password'],
        )
        confirmation_code = confirm_registration(user.email)
        user.confirmation_code = confirmation_code
        user.save()
        return user

    def password_confirm(self):
        if self.data.get('password_confirm') and self.data['password_confirm'] != self.cleaned_data['password']:
            raise ValidationError("Пароли не совпадают")

    def user_presence(self):
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise ValidationError("Пользователь с такой почтой уже существует")
