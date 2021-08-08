from django import forms
from .models import Personne


class PersonneForm(forms.ModelForm):
    class Meta:
        model = Personne
        fields = ['nom', 'prenom', 'date_naissance', 'sexe', 'adresse', 'email', 'telephone']
        labels = {'nom':'Nom', 'prenom':'Prénom', 'date_naissance':'Date de naissance', 'sexe':'Sexe', 'email':'E-mail', 'telephone':'Téléphone'}
        widgets = {
            'nom': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Votre nom...'}),
            'prenom': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Votre prénom...'}),
            'date_naissance': forms.DateInput(attrs={'class':'form-control', 'type':'date', 'placeholder':'Votre date de naissance...'}),
            'sexe': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Votre sexe...'}),
            'adresse': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Rue...'}),
            'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Votre e-mail...'}),
            'telephone': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Votre téléphone...'}),

            



        }