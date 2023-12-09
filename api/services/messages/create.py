from django import forms
from rest_framework.exceptions import ValidationError
from service_objects.fields import ModelField
from service_objects.services import ServiceWithResult

from models_app.models import Workspace, User, Message

TYPES = {
    'channel': 'channel_id',
    'direct': 'direct_id'
}


class MessageCreateService(ServiceWithResult):
    workspace_id = forms.IntegerField()
    item_id = forms.IntegerField()
    type = forms.CharField()
    text = forms.CharField()
    author = ModelField(User)

    custom_validations = ["workspace_presence", ]

    def process(self):
        self.run_custom_validations()
        self.result = self._messages_create
        return self

    @property
    def _messages_create(self):
        params = {
            TYPES[self.cleaned_data['type']]: self.cleaned_data['item_id'],
            'text': self.cleaned_data['text'],
            'workspace_id': self.cleaned_data['workspace_id'],
            'author': self.cleaned_data['author']
        }
        return Message.objects.create(**params)

    def workspace_presence(self):
        workspace = Workspace.objects.filter(id=self.cleaned_data['workspace_id'])
        if not workspace.exists():
            raise ValidationError("Рабочего пространства с таким id не существует")
        return workspace.first()
