from django import forms
from . import models

class CreateLesson(forms.ModelForm): # create own form
    class Meta:
        model = models.Lesson
        fields = ['title', 'body', 'slug', 'thumb']
