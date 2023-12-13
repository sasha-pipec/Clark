from django import forms
from service_objects.fields import ModelField
from service_objects.services import ServiceWithResult

from models_app.models import User, Channel


class ChannelAddUserService(ServiceWithResult):
    id = forms.IntegerField()
    user = ModelField(User)

    def process(self):
        self.result = self._channel_add_user
        return self

    @property
    def _channel_add_user(self):
        channel = Channel.objects.get(id=self.cleaned_data['id'])
        channel.users.add(self.cleaned_data['user'])
        channel.save()
        return channel
