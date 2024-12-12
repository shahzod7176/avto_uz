from django import forms
from main.models import Car


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['name', 'produced_year', 'color', 'price', 'case', 'location', 'brand', 'fuel', 'category']
