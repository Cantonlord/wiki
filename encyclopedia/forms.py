from django import forms

# Search form
class SearchForm(forms.Form):
    q = forms.CharField(label='', max_length=255, widget=forms.TextInput(attrs={
        'class': 'search',
        'placeholder': "Search Encyclopedia"
    }))

class CreateForm(forms.Form):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class': 'title',
        'placeholder': "Title..."
    }))
    content = forms.CharField(label='', widget=forms.Textarea(attrs={
        'class': 'content',
        'placeholder': "Content..."
    }))
    
class EditForm(forms.Form):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class': 'title'
    }))
    content = forms.CharField(label='', widget=forms.Textarea(attrs={
        'class': 'content'
    }))