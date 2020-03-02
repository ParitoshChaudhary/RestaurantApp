from django import forms
from menu_app.models import Item


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'cuisine', 'category', 'cost']