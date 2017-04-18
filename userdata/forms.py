from django import forms
from allauth.account.forms import LoginForm, SignupForm


class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        self.fields['login'].label = ''
        self.fields['login'].widget = forms.TextInput(attrs={
            'placeholder': 'Username',
            'autofocus': 'autofocus',
            'class': 'form-control',
            })
        self.fields['password'].label = ''
        self.fields['password'].widget = forms.PasswordInput(attrs={
            'placeholder': 'Password',
            'class': 'form-control',
            })


class CustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super(CustomSignupForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = ''
        self.fields['username'].widget = forms.TextInput(attrs={
            'placeholder': 'Username',
            'autofocus': 'autofocus',
            'class': 'form-control',
            })
        self.fields['email'].label = ''
        self.fields['email'].widget = forms.TextInput(attrs={
            'placeholder': 'E-mail address',
            'class': 'form-control',
            })
        self.fields['password1'].label = ''
        self.fields['password1'].widget = forms.PasswordInput(attrs={
            'placeholder': 'Password',
            'class': 'form-control',
            })
        self.fields['password2'].label = ''
        self.fields['password2'].widget = forms.PasswordInput(attrs={
            'placeholder': 'Password (again)',
            'class': 'form-control',
            })
