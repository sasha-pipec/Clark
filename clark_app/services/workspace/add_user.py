from django import forms
from service_objects.fields import ModelField
from service_objects.services import ServiceWithResult

from models_app.models import Workspace, User


class WorkspaceAddUserService(ServiceWithResult):
    id = forms.IntegerField()
    user = ModelField(User)

    def process(self):
        self.result = self._workspace_add_user
        return self

    @property
    def _workspace_add_user(self):
        workspace = Workspace.objects.get(id=self.cleaned_data['id'])
        if self.cleaned_data['user'] not in workspace.users.all():
            workspace.users.add(self.cleaned_data['user'])
        return workspace
