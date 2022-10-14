from django.db import models


class Status(models.Model):
    name = models.CharField(verbose_name='Название', max_length=20)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Изменено', auto_now=True)

    def __str__(self) -> str:
        return f'{self.name}'
