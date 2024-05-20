from django import forms
from .models import Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title', 'description','image']

class SearchForm(forms.Form):
    query = forms.CharField(label='Search',max_length=100)
