from django.db import models
from django.urls import reverse


class Task(models.Model):
    summary = models.CharField(
        verbose_name='Краткое описание',
        max_length=100
        )
    description = models.TextField(
        verbose_name='Полное описание',
        max_length=600,
        null=True,
        blank=True
        )
    status = models.ForeignKey(
        to='webapp.Status',
        verbose_name='Статус',
        related_name='tasks',
        default='New',
        on_delete=models.RESTRICT
        )
    created_at = models.DateTimeField(
        verbose_name='Создано',
        auto_now_add=True
        )
    updated_at = models.DateTimeField(
        verbose_name='Изменено',
        auto_now=True)
    type = models.ManyToManyField(
        to='webapp.Type',
        verbose_name='Тип',
        related_name='tasks',
        blank=True
        )

    def get_absolute_url(self):
        return reverse('task_detail', kwargs={'pk': self.pk})
