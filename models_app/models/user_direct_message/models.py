from django.db import models


class UserDirectMessage(models.Model):
    user = models.ForeignKey(to='User', on_delete=models.CASCADE, verbose_name='Пользователь')
    direct_message = models.ForeignKey(to='DirectMessage', on_delete=models.CASCADE, verbose_name='Личные сообщения')

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = 'user_direct_message'
        app_label = 'models_app'
        verbose_name = 'UserDirectMessage'
        verbose_name_plural = 'UserDirectMessages'
