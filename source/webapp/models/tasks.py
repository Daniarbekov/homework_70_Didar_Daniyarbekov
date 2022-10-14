from django.db import models
from django.urls import reverse
from django.utils import timezone
from webapp.managers import TaskManager


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
    is_deleted = models.BooleanField(
        verbose_name='Удалено', 
        default=False, null=False
        )
    deleted_at = models.DateTimeField(
        verbose_name='Дата удаления',
        null=True,
        default=None
        )
    project = models.ForeignKey(
        to='webapp.Project',
        verbose_name='Проект',
        related_name='tasks',
        default='1',
        on_delete=models.CASCADE
        )
    
    objects = TaskManager()
    
    def get_absolute_url(self):
        return reverse('task_detail', kwargs={'pk': self.pk})

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()
        self.is_deleted = True
        self.save()
