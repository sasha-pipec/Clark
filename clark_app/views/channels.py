from django.shortcuts import redirect, render
from django.views import View
from service_objects.services import ServiceOutcome

from clark_app.services.channel.add_user import ChannelAddUserService
from clark_app.services.channel.create import ChannelCreateService
from clark_app.services.channel.exit_user import ChannelExitUserService
from clark_app.services.channel.list_to_user import ChannelListService


class ChannelListCreateView(View):

    def get(self, request, *args, **kwargs):
        outcome = ServiceOutcome(ChannelListService, kwargs | request.GET.dict() | {'user': request.user})
        return render(request, 'clark_app/channels.html', context={
            'channels': outcome.result,
            'workspace_id': kwargs['id']
        })

    def post(self, request, *args, **kwargs):
        ServiceOutcome(ChannelCreateService, kwargs | request.POST.dict() | {'user': request.user})
        return redirect('workspace_detail', kwargs['id'])


class ChannelAddUserView(View):

    def get(self, request, *args, **kwargs):
        ServiceOutcome(ChannelAddUserService, kwargs | {'user': request.user})
        return redirect('workspace')


class ChannelExitUserView(View):

    def get(self, request, *args, **kwargs):
        ServiceOutcome(ChannelExitUserService, kwargs | {'user': request.user})
        return redirect('workspace')