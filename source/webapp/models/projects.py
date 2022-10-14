from django.db import models
from django.urls import reverse

class Project(models.Model):
    name = models.CharField(verbose_name='Название', max_length=30)
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    start_date = models.DateField(verbose_name='Дата начала')
    end_date = models.DateField(verbose_name='Дата окончания', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='Создано',auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Изменено',auto_now=True)
    
    def __str__(self) -> str:
        return f'{self.name}'
    
    def get_absolute_url(self):
        return reverse('project_detail', kwargs={'pk': self.pk})
