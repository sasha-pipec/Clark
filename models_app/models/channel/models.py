from django.db import models

from models_app.models.abstract_time.models import AbstractTime


class Channel(AbstractTime):
    name = models.CharField(max_length=255, verbose_name='Название')
    users = models.ManyToManyField(to='User', through='UserChannel', verbose_name='Участники')
    workspace = models.ForeignKey(to='Workspace', on_delete=models.CASCADE, related_name='channels', verbose_name='Рабочее пространство')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'channel'
        app_label = 'models_app'
        verbose_name = 'Channel'
        verbose_name_plural = 'Channels'
