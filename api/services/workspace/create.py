from rest_framework.exceptions import ValidationError
from service_objects.fields import ModelField
from service_objects.services import ServiceWithResult
from django import forms

from models_app.models import Workspace, User, Channel

MAX_WORKSPACE_COUNT = 2
DEFAULT_CHANNEL_NAME = 'Общий'


class WorkspaceCreateService(ServiceWithResult):
    name = forms.CharField()
    about = forms.CharField()
    image = forms.ImageField()
    owner = ModelField(User)

    custom_validations = ['_count_workspace']

    def process(self):
        self.run_custom_validations()
        self.result = self._workspace_create
        return self

    @property
    def _workspace_create(self):
        workspace = Workspace.objects.create(
            name=self.cleaned_data['name'],
            about=self.cleaned_data['about'],
            image=self.cleaned_data['image'],
            owner=self.cleaned_data['owner']
        )
        workspace.users.add(self.cleaned_data['owner'])
        workspace.save()
        self._channel__create(workspace)
        return workspace

    def _channel__create(self, workspace):
        channel = Channel.objects.create(name=DEFAULT_CHANNEL_NAME, workspace=workspace)
        channel.users.add(self.cleaned_data['owner'])
        channel.save()

    def _count_workspace(self):
        workspaces = Workspace.objects.filter(owner=self.cleaned_data['owner'])
        if workspaces.count() >= MAX_WORKSPACE_COUNT:
            raise ValidationError('Один пользователь не может иметь больше 2 рабочих пространств')
