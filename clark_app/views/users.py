from django.db import transaction
from django.shortcuts import redirect, render
from django.views import View
from service_objects.services import ServiceOutcome

from api.services.user.create import UserCreateService


class UserCreateView(View):

    @transaction.atomic
    def post(self, request):
        try:
            ServiceOutcome(UserCreateService, request.POST)
        except Exception as error:
            return render(request, 'clark_app/registration.html', context={
                'error': error.detail[0]
            })
        return redirect('confirm')
