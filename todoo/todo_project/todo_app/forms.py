from .models import tasks
from django import forms

class model(forms.ModelForm):
    class Meta:
        model = tasks
        fields = ['heading', 'description', 'date', 'time']
