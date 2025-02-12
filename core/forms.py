from django import forms

from .models import FileModel

class ModelFileForm(forms.ModelForm):
    class Meta:
        model = FileModel
        fields = ['file']
        #widgets = {    'file': forms.ClearableFileInput(attrs={'multiple': True})}
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['file'].widget.attrs.update({'multiple': True})