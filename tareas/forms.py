from django import forms
from django.forms import ModelForm

from .models import *


class TareaForm(forms.ModelForm):
    # Para colocar un Placeholder
    titulo = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Agrega una tarea...'}))

    class Meta:
        model = Tarea
        fields = '__all__'
