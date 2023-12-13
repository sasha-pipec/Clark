from django import forms
from django.db.models import Q
from service_objects.services import ServiceWithResult

from models_app.models import User, DirectMessage, UserDirectMessage


class DirectAddUserService(ServiceWithResult):
    id = forms.IntegerField()
    current_email = forms.EmailField()
    email = forms.EmailField()

    def process(self):
        self.result = self._direct_add_user
        return self

    @property
    def _direct_add_user(self):
        directs = DirectMessage.objects.filter(
            workspace_id=self.cleaned_data['id']
        )
        direct = UserDirectMessage.objects.filter(
            Q(direct_message_id__in=directs.values_list('id', flat=True)) &
            Q(user__email=self.cleaned_data['current_email']) |
            Q(user__email=self.cleaned_data['email'])
        )
        if not direct.exists() or direct.count() < 2:
            direct = DirectMessage.objects.create(
                workspace_id=self.cleaned_data['id']
            )
            sender = User.objects.get(email=self.cleaned_data['current_email'])
            receiver = User.objects.get(email=self.cleaned_data['email'])
            direct.users.set([sender, receiver])
            direct.save()
        return direct
