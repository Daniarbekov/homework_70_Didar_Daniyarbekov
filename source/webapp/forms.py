from django import forms
from webapp.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['summary', 'type', 'status', 'description']
        widgets = {
            'type': forms.CheckboxSelectMultiple
        }
