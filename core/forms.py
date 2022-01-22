from django import forms

from core.models import Documents


class DocsForm(forms.ModelForm):
    class Meta:
        model = Documents
        fields = ('text', 'date', 'date_answer', 'fio', 'category')
