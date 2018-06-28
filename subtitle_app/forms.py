from django import forms
from .models import Document,Translate

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', )


class TranslateForm(forms.Form):
    id = forms.IntegerField(widget=forms.HiddenInput())
    suggestion = forms.CharField()
