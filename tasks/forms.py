from asyncio import Task
from ctypes import resize
from dataclasses import fields
from pyexpat import model
from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'important']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write a title'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Write a description'}),
            'important': forms.CheckboxInput(attrs={'class': 'form-check-input'})            
        }