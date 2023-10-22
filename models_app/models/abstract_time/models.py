from django.db import models


class AbstractTime(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return self.created_at

    class Meta:
        abstract = True
        db_table = 'abstract_time'
        app_label = 'models_app'
        verbose_name = 'AbstractTime'
        verbose_name_plural = 'AbstractTimes'
