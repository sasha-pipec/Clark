from service_objects.services import ServiceWithResult
from django import forms
from django.contrib.auth import authenticate, login

class UserLoginService(ServiceWithResult):
    email = forms.EmailField(required=False)
    password = forms.CharField(required=False)

    def process(self):
        self.result = self._user_login()
        return self

    def _user_authenticate(self):
        return authenticate(
                  self.data['request'],
                  email=self.cleaned_data['email'],
                  password=self.cleaned_data['password']
              )
    
    def _user_login(self):
        user = self.data.get('user')
        if not user:
          user = self._user_authenticate()
        if user is not None:
            login(self.data['request'], user)
        return user