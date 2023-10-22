from django.db import models


class UserChannel(models.Model):
    user = models.ForeignKey(to='User', on_delete=models.CASCADE, verbose_name='Пользователь')
    channel = models.ForeignKey(to='Channel', on_delete=models.CASCADE, verbose_name='Канал')

    def __str__(self):
        return f'{self.user.username} -- {self.channel.name}'

    class Meta:
        db_table = 'user_channel'
        app_label = 'models_app'
        verbose_name = 'UserChannel'
        verbose_name_plural = 'UserChannels'
