from django.db import models

from models_app.models.abstract_time.models import AbstractTime


class DirectMessage(AbstractTime):
    users = models.ManyToManyField(to='User', through='UserDirectMessage', verbose_name='Участники')
    workspace = models.ForeignKey(to='Workspace', on_delete=models.CASCADE, related_name='direct_messages', verbose_name='Рабочее пространство')

    def __str__(self):
        return self.workspace.name

    class Meta:
        db_table = 'direct_message'
        app_label = 'models_app'
        verbose_name = 'DirectMessage'
        verbose_name_plural = 'DirectMessages'
