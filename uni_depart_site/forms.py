from django import forms

class SearchForm(forms.Form):
    search_keyword = forms.CharField(label='')