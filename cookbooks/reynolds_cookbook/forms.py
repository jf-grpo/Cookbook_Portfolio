# forms.py
from django import forms
from .models import Entree, Dessert, SoupStewChili, Ingredient, Instruction

from django.forms import inlineformset_factory

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



IngredientFormSet = inlineformset_factory(
    Entree, Ingredient, fields=['name', 'quantity', 'unit'], extra=1, can_delete=True
)

InstructionFormSet = inlineformset_factory(
    Entree, Instruction, fields=['step_number', 'description'], extra=1, can_delete=True
)
