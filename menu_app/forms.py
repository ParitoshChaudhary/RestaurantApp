from django import forms
from menu_app.models import Item, Category, Cuisine


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'cost']


class CategoryForm(forms.Form):
    class Meta:
        model = Category
        # fields = forms.ModelChoiceField(queryset=Category.objects.filter(id=1), empty_label='-----', widget=forms.Select)
        # fields = ['category_type']
        fields = forms.ModelChoiceField(queryset=Category.objects.order_by('category_type')
                                        .values_list('category_type', flat=True).distinct(), empty_label='-----')


class CuisineForm(forms.ModelForm):
    class Meta:
        model = Cuisine
        # fields = forms.ModelChoiceField(queryset=Cuisine.objects.filter(id=1), empty_label='-----',
        #                                 widget=forms.Select)
        # fields = forms.ModelChoiceField(queryset=Cuisine.objects.order_by('cuisine')
        #                                 .values_list('cuisine', flat=True).distinct(), empty_label='-----')
        fields = ['cuisine']