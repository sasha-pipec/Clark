from service_objects.fields import ModelField
from service_objects.services import ServiceWithResult
from django import forms

from models_app.models import Workspace, User


class WorkspaceCreateService(ServiceWithResult):
    name = forms.CharField()
    about = forms.CharField()
    image = forms.ImageField()
    owner = ModelField(User)

    def process(self):
        self.result = self._workspace_create
        return self

    @property
    def _workspace_create(self):
        return Workspace.objects.create(
            name=self.cleaned_data['name'],
            about=self.cleaned_data['about'],
            image=self.cleaned_data['image'],
            owner=self.cleaned_data['owner']
        )
