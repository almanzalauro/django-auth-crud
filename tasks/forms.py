from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'important']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Escriba un titulo'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Escriba un descripcion'}),
            'important': forms.CheckboxInput(attrs={'class': 'form-check-inpur text-center'}),
            
        }
        #con widgets, lo que hago es ponerle las clases de bootstrap como atributos, ya que no son tipo html este tipo de form, porque fue creado con codigo python