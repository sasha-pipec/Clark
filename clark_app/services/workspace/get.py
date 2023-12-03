from django import forms
from service_objects.services import ServiceWithResult

from models_app.models import Workspace


class WorkspaceDetailService(ServiceWithResult):
    id = forms.IntegerField()

    def process(self):
        self.result = self._workspace_get
        return self

    @property
    def _workspace_get(self):
        return Workspace.objects.get(id=self.cleaned_data['id'])
