from django import forms

# Search form
class SearchForm(forms.Form):
    query = forms.CharField(label='', max_length=255, widget=forms.TextInput(attrs={
        'class': 'search',
        'placeholder': "Search Encyclopedia"
    }))