from django import forms

from core.models import Documents


class DocsForm(forms.ModelForm):
    class Meta:
        model = Documents
        fields = ('category', 'text', 'date', 'date_answer', 'fio')
