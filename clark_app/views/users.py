from django.contrib.auth import authenticate, login
from django.db import transaction
from django.shortcuts import redirect, render
from django.views import View
from service_objects.services import ServiceOutcome

from api.services.user.confirm_email import UserConfirmEmailService
from api.services.user.create import UserCreateService


class UserCreateLoginView(View):

    def get(self, request):
        user = authenticate(request, email=request.GET['email'], password=request.GET['password'])
        if user is not None:
            login(request, user)
            return redirect('workspace')
        return render(request, 'clark_app/authorization.html', context={
            'error': 'Неверная почта или пароль'
        })

    @transaction.atomic
    def post(self, request):
        try:
            ServiceOutcome(UserCreateService, request.POST)
        except Exception as error:
            return render(request, 'clark_app/registration.html', context={
                'error': error.detail[0]
            })
        return redirect('confirm')


class UserConfirmEmailView(View):

    def post(self, request):
        try:
            outcome = ServiceOutcome(UserConfirmEmailService, request.POST)
        except Exception as error:
            return render(request, 'clark_app/confirm_email.html', context={
                'error': error.detail[0]
            })
        login(request, outcome.result)
        return redirect('workspace')
