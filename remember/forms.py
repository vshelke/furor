from django import forms

class EntryForm(forms.Form):
    name = forms.CharField(label='Name', max_length=128, widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Name your memory!'}))
    link = forms.URLField(label='Link', required=False, widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Link to save!'}))
    tag = forms.CharField(label='Tag', max_length=20, widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'To keep your memories organised'}))
    desc = forms.CharField(label='Description', max_length=512, widget=forms.Textarea(attrs={'class': 'textarea', 'placeholder': 'To remember for what it was...'}))

class SignupForm(forms.Form):
    username = forms.CharField(label='Username', max_length=128 ,widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'input'}))
    first_name = forms.CharField(label='First Name', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'First name','class': 'input'}))
    last_name = forms.CharField(label='Last Name', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Last name','class': 'input'}))
    email = forms.EmailField(label='Email', max_length=512, widget=forms.TextInput(attrs={'placeholder': 'Email','class': 'input'}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'placeholder': 'Password','class': 'input'}) , max_length=50)

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=128, widget=forms.TextInput(attrs={'placeholder': 'Username','class': 'input'}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'placeholder': 'Password','class': 'input'}) , max_length=50)
