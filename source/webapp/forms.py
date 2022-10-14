from django import forms
from webapp.models import Task
from webapp.models import Project
from django.forms.widgets import  TextInput


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'start_date', 'end_date', 'description']
        widgets = {
            'start_date': TextInput(attrs={'type':'date'}),
            'end_date': TextInput(attrs={'type':'date'})
        }


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['summary', 'type', 'status', 'description']
        widgets = {
            'type': forms.CheckboxSelectMultiple
        }


class SearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label='Найти')
