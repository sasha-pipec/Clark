from django.db import models


class UserWorkspace(models.Model):
    user = models.ForeignKey(to='User', on_delete=models.CASCADE, related_name='workspaces', verbose_name='Пользователь')
    workspace = models.ForeignKey(to='Workspace', on_delete=models.CASCADE, related_name='workspaces', verbose_name='Рабочее пространство')

    def __str__(self):
        return f'{self.user.username} -- {self.workspace.name}'

    class Meta:
        db_table = 'user_workspace'
        app_label = 'models_app'
        verbose_name = 'UserWorkspace'
        verbose_name_plural = 'UserWorkspaces'
