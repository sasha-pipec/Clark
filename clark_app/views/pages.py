from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View
from service_objects.services import ServiceOutcome

from api.services.direct_messages.list_to_user import DirectListToUserService
from clark_app.services.workspace.get import WorkspaceDetailService


class MainPageView(View):

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('workspace')
        return render(request, 'clark_app/main.html')


class AuthPageView(View):

    def get(self, request):
        return render(request, 'clark_app/authorization.html')


class RegisterPageView(View):

    def get(self, request):
        return render(request, 'clark_app/registration.html')


class ConfirmEmailPageView(View):

    def get(self, request):
        return render(request, 'clark_app/confirm_email.html')


class WorkspacePageView(View):

    @method_decorator(login_required(login_url='auth'))
    def get(self, request):
        if request.session.get('error'):
            error = request.session['error']
            del request.session['error']
            return render(request, 'clark_app/workspaces.html', context={
                'error': error
            })
        # if request.session.get('active_workspace'):
        #     return redirect('workspace_detail', request.session['active_workspace'])
        return render(request, 'clark_app/workspaces.html')


class WorkspaceDetailPageView(View):

    @method_decorator(login_required(login_url='auth'))
    def get(self, request, id):
        request.session['active_workspace'] = id
        outcome = ServiceOutcome(WorkspaceDetailService, {'id': id})
        directs = ServiceOutcome(DirectListToUserService, {
            'workspace_id': outcome.result.id,
            'user': request.user
        })
        return render(request, 'clark_app/workspace.html', context={
            'workspace': outcome.result,
            'directs': directs.result
        })
