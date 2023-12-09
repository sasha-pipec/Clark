from django.db import transaction
from django.shortcuts import redirect, render
from django.views import View
from service_objects.services import ServiceOutcome

from api.services.user.confirm_email import UserConfirmEmailService
from api.services.user.create import UserCreateService

from clark_app.services.user.login import UserLoginService


class UserLoginView(View):

    def post(self, request):
        outcome = ServiceOutcome(UserLoginService, request.POST.dict() | {'request': request})
        if outcome.result:
            return redirect('workspace')
        return render(request, 'clark_app/authorization.html', context={
            'error': 'Неверная почта или пароль'
        })


class UserCreateView(View):

    @transaction.atomic
    def post(self, request):
        try:
            ServiceOutcome(UserCreateService, request.POST.dict())
        except Exception as error:
            return render(request, 'clark_app/registration.html', context={
                'error': error.detail[0]
            })
        return redirect('confirm')


class UserConfirmEmailView(View):

    def post(self, request):
        try:
            outcome = ServiceOutcome(UserConfirmEmailService, request.POST.dict())
        except Exception as error:
            return render(request, 'clark_app/confirm_email.html', context={
                'error': error.detail[0]
            })
        ServiceOutcome(UserLoginService, request.POST.dict() | {'request': request,
                                                                'user': outcome.result})
        return redirect('workspace')
