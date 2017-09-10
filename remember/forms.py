from django import forms

class EntryForm(forms.Form):
    name = forms.CharField(label='Name', max_length=128, widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Name your memory!'}))
    link = forms.URLField(label='Link', widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Link to save!'}))
    tag = forms.CharField(label='Tag', max_length=20, widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'To keep your memories organised'}))
    desc = forms.CharField(label='Description', max_length=512, widget=forms.Textarea(attrs={'class': 'textarea', 'placeholder': 'To remember for what it was...'}))
