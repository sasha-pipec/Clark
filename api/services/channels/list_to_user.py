from functools import lru_cache

from django import forms
from rest_framework.exceptions import ValidationError
from service_objects.fields import ModelField
from service_objects.services import ServiceWithResult

from models_app.models import Workspace, User


class ChannelsListToUserService(ServiceWithResult):
    workspace_id = forms.IntegerField()
    user = ModelField(User)

    custom_validations = ["workspace_presence", ]

    def process(self):
        self.run_custom_validations()
        self.result = self._channels_list
        return self

    @property
    def _channels_list(self):
        workspace = self.workspace_presence()
        return workspace.channels.filter(users=self.cleaned_data['user'])

    @lru_cache()
    def workspace_presence(self):
        workspace = Workspace.objects.filter(id=self.cleaned_data['workspace_id'])
        if not workspace.exists():
            raise ValidationError("Рабочего пространства с таким id не существует")
        return workspace.first()
