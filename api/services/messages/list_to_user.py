from functools import lru_cache

from django import forms
from rest_framework.exceptions import ValidationError
from service_objects.services import ServiceWithResult

from models_app.models import Workspace

TYPES = {
    'channel': 'channel_id',
    'direct': 'direct_id'
}


class MessageListToUserService(ServiceWithResult):
    workspace_id = forms.IntegerField()
    item_id = forms.IntegerField()
    type = forms.CharField()

    custom_validations = ["workspace_presence", ]

    def process(self):
        self.run_custom_validations()
        self.result = self._messages_list
        return self

    @property
    def _messages_list(self):
        workspace = self.workspace_presence()
        filters = {
            TYPES[self.cleaned_data['type']]: self.cleaned_data['item_id'],
            'workspace_id': self.cleaned_data['workspace_id']
        }
        return workspace.workspace_messages.filter(**filters)

    @lru_cache()
    def workspace_presence(self):
        workspace = Workspace.objects.filter(id=self.cleaned_data['workspace_id'])
        if not workspace.exists():
            raise ValidationError("Рабочего пространства с таким id не существует")
        return workspace.first()
