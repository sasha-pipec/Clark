from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views import View
from service_objects.services import ServiceOutcome

from api.services.workspace.create import WorkspaceCreateService


class WorkspaceCreateView(View):

    @method_decorator(login_required(login_url='auth'))
    def post(self, request):
        outcome = ServiceOutcome(WorkspaceCreateService, request.POST.dict() | {'owner': request.user}, request.FILES)
        return redirect('workspace_detail', outcome.result.id)
