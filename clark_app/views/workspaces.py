from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views import View
from service_objects.services import ServiceOutcome

from api.services.workspace.create import WorkspaceCreateService
from clark_app.services.workspace.add_user import WorkspaceAddUserService


class WorkspaceCreateExitView(View):

    def get(self, request):
        if request.session.get('active_workspace'):
            del request.session['active_workspace']
        return redirect('workspace')

    @method_decorator(login_required(login_url='auth'))
    def post(self, request):
        try:
            outcome = ServiceOutcome(WorkspaceCreateService, request.POST.dict() | {'owner': request.user}, request.FILES)
            return redirect('workspace_detail', outcome.result.id)
        except Exception as error:
            request.session['error'] = error.detail[0]
            return redirect('workspace')


class WorkspaceAddUserView(View):
    @method_decorator(login_required(login_url='auth'))
    def get(self, request, *args, **kwargs):
        ServiceOutcome(WorkspaceAddUserService, kwargs | {'user': request.user})
        return redirect('workspace')
