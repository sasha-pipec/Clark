from django import forms
from django.db.models import Count
from service_objects.fields import ModelField
from service_objects.services import ServiceWithResult

from models_app.models import User, Channel


class ChannelListService(ServiceWithResult):
    id = forms.IntegerField()
    user = ModelField(User)
    search = forms.CharField(required=False)

    def process(self):
        self.result = self._channel_list
        return self

    @property
    def _channel_list(self):
        channels = Channel.objects.filter(
            workspace_id=self.cleaned_data['id']
        ).annotate(count=Count('users')).exclude(users=self.cleaned_data['user'])
        if self.cleaned_data.get('search'):
            channels = channels.filter(name__icontains=self.cleaned_data['search'])
        return channels
