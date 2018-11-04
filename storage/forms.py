from django import forms
from .models import FileModel


class FileForm(forms.Form):
    file = forms.FileField()

    def save(self):
        file = FileModel(**self.cleaned_data)
        file.save()
        return file
