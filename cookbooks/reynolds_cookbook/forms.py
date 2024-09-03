# forms.py
from django import forms
from .models import Entree, Dessert, SoupStewChili

class EntreeForm(forms.ModelForm):
    class Meta:
        model = Entree
        fields = ['title', 'author', 'main_feature']

class DessertForm(forms.ModelForm):
    class Meta:
        model = Dessert
        fields = ['title', 'author', 'dessert_type']

class SoupStewChiliForm(forms.ModelForm):
    class Meta:
        model = SoupStewChili
        fields = ['title', 'author', 'soup_type']
