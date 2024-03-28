from django import forms
import models


class UploadForm(forms.ModelForm):
    """
    Форма для загрузки нескольких документов
    """
    attachments = models.Files(
        widget=forms.ClearableFileInput(attrs={'multiple': True})
        )
