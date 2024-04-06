from django import forms


class SignUpForm(forms.Form):
    username = forms.CharField(label='Username', max_length=50,
                               error_messages={'max_length': 'Max amount of symbols is 50'})
    password = forms.CharField(label='Password', max_length=50, widget=forms.PasswordInput,
                               error_messages={'max_length': 'Max amount of symbols is 50'})
    email = forms.EmailField(label='Email', max_length=50)


class CodeVerificationForm(forms.Form):
    code = forms.CharField(label='Code', max_length=10)
