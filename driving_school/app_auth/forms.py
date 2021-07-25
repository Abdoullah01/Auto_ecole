from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField(label="E-mail", widget= forms.TextInput(attrs= {'class': 'form-control'}) )
    pwd = forms.CharField(label="Mot de passe", widget=forms.PasswordInput(attrs= {'class': 'form-control'}))
    
    
    
class RegisterForm(forms.Form):
    email = forms.EmailField(label="E-mail", widget= forms.TextInput(attrs= {'class': 'form-control'}))
    pwd = forms.CharField(label="Mot de passe", widget=forms.PasswordInput(attrs= {'class': 'form-control'}))
    pwd_confirm = forms.CharField(label="Mot de passe de confirmation", widget=forms.PasswordInput(attrs= {'class': 'form-control'}))