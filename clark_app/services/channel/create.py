from django import forms
from service_objects.fields import ModelField
from service_objects.services import ServiceWithResult

from models_app.models import User, Channel


class ChannelCreateService(ServiceWithResult):
    id = forms.IntegerField()
    name = forms.CharField()
    description = forms.CharField()
    user = ModelField(User)

    def process(self):
        self.result = self._channel_create
        return self

    @property
    def _channel_create(self):
        channel = Channel.objects.create(
            name=self.cleaned_data['name'],
            description=self.cleaned_data['description'],
            workspace_id=self.cleaned_data['id']
        )
        channel.users.add(self.cleaned_data['user'])
        channel.save()
        return channel
