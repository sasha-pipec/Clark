from django.db import models

from models_app.models.abstract_time.models import AbstractTime


class Workspace(AbstractTime):
    name = models.CharField(max_length=255, verbose_name='Название')
    about = models.TextField(verbose_name='Чем занимается')
    image = models.ImageField(upload_to='workspaces/', verbose_name='Изображение')
    owner = models.ForeignKey(to='User', on_delete=models.CASCADE, related_name='workspase_set', verbose_name='Владелец')
    users = models.ManyToManyField(to='User', through='UserWorkspace', related_name='workspace_user_set', verbose_name='Участники')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'workspace'
        app_label = 'models_app'
        verbose_name = 'Workspace'
        verbose_name_plural = 'Workspaces'
