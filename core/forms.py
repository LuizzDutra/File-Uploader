from django import forms

from .models import FileModel

class ModelFileForm(forms.ModelForm):
    class Meta:
        model = FileModel
        fields = ['file']