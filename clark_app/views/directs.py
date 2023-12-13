from django.shortcuts import redirect
from django.views import View
from service_objects.services import ServiceOutcome

from clark_app.services.directs.add_user import DirectAddUserService


class DirectsAddUserView(View):

    def post(self, request, *args, **kwargs):
        ServiceOutcome(DirectAddUserService, kwargs | request.POST.dict())
        return redirect('workspace')