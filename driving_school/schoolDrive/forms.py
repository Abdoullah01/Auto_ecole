from django import forms
from .models import Personne


class PersonneForm(forms.ModelForm):
    class Meta:
        model = Personne
        fields = ['nom', 'prenom', 'date_naissance', 'sexe', 'adresse', 'email', 'telephone']
        labels = {'nom':'Nom', 'prenom':'Prénom', 'date_naissance':'Date de naissance', 'sexe':'Sexe', 'email':'E-mail', 'telephone':'Téléphone'}
        widgets = {
            'nom': forms.TextInput(attrs={'class':'form-control'}),
            'prenom': forms.TextInput(attrs={'class':'form-control'}),
            'date_naissance': forms.DateInput(attrs={'class':'form-control'}),
            'sexe': forms.TextInput(attrs={'class':'form-control'}),
            'adesse': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'telephone': forms.NumberInput(attrs={'class':'form-control'}),

            



        }