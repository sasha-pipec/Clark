from django.db import models

from models_app.models.abstract_time.models import AbstractTime


class Message(AbstractTime):
    text = models.TextField(verbose_name='Текст')
    file = models.FileField(upload_to='messages/', blank=True, null=True, verbose_name='Файл')
    answer_to = models.ForeignKey(to='Message', on_delete=models.CASCADE, blank=True, null=True, verbose_name='Ответ на')
    author = models.ForeignKey(to='User', on_delete=models.CASCADE, verbose_name='Автор')
    direct = models.ForeignKey(to='DirectMessage', on_delete=models.CASCADE, blank=True, null=True, related_name='direct_messages',
                               verbose_name='Личное сообщение')
    channel = models.ForeignKey(to='Channel', on_delete=models.CASCADE, blank=True, null=True, related_name='chanel_messages',
                                verbose_name='Сообшение канала')
    workspace = models.ForeignKey(to='Workspace', on_delete=models.CASCADE, related_name='workspace_messages',
                                verbose_name='Сообшение рабочего пространства')

    def __str__(self):
        return f'{self.author.email} -- {self.text}'

    class Meta:
        db_table = 'message'
        app_label = 'models_app'
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'
