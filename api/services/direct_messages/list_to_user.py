from functools import lru_cache

from django import forms
from rest_framework.exceptions import ValidationError
from service_objects.fields import ModelField
from service_objects.services import ServiceWithResult

from models_app.models import Workspace, User


class DirectListToUserService(ServiceWithResult):
    workspace_id = forms.IntegerField()
    user = ModelField(User)

    custom_validations = ["workspace_presence", ]

    def process(self):
        self.run_custom_validations()
        self.result = self._directs_list
        return self

    @property
    def _directs_list(self) -> [User]:
        workspace = self.workspace_presence()
        receiver_list = []
        directs = workspace.direct_messages.filter(users=self.cleaned_data['user'])
        for direct in directs:
            direct_id = direct.id
            receiver = direct.users.all().exclude(email=self.cleaned_data['user'].email)
            if receiver.exists():
                receiver = receiver.first()
                receiver.direct_id=direct_id
                receiver.save()
                receiver_list.append(receiver)
        return receiver_list

    @lru_cache()
    def workspace_presence(self):
        workspace = Workspace.objects.filter(id=self.cleaned_data['workspace_id'])
        if not workspace.exists():
            raise ValidationError("Рабочего пространства с таким id не существует")
        return workspace.first()
