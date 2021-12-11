from django import forms
from .models import Todo

class TodoCreationForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['name','due_date']
