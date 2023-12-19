from .models import Table
from django.forms import ModelForm, TextInput, NumberInput


class TableForm(ModelForm):
    class Meta:
        model = Table
        fields = ["title", "country", "year", "GDP"]
        widgets = {
            "title": TextInput(attrs = {
                'class': 'form-control',
                'placeholder': 'Введіть назву статистики',
            }),
            "country": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть країну',
            }),
            "year": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть рік',
            }),
            "GDP": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть значення',
            }),
        }