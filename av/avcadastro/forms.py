from django import forms
from .models import NotaFilial


class NotaFilialForm(forms.ModelForm):
    class Meta:
        model = NotaFilial
        fields = ['periodo', 'nota']


class NotaFilialFormEx(forms.ModelForm):
    periodo = forms.CharField(disabled=True)
    nota = forms.CharField(disabled=True)

    class Meta:
        model = NotaFilial
        fields = ['periodo', 'nota']
