from django.db import models
from django.db.models.fields import EmailField

# Create your models here.

class Personne(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    date_naissance = models.DateField()
    sexe = models.CharField(max_length=15)
    adresse = models.IntegerField()
    email = models.EmailField()
    
    def __str__(self):
        return self.nom
    
class Vehicule(models.Model):
    marque = models.CharField(max_length=60)
    type = models.CharField(max_length=50)
    
    def __str__(self):
        return self.marque
    
class Cours(models.Model):
    date_seance = models.DateField()
    horaire = models.DateTimeField(auto_now=True)
    type_formation = models.CharField(max_length=50)
    vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE)
    personne = models.ForeignKey(Personne, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.date_seance
    
    
class Moniteur(Personne):
    date_rcrutement = models.DateField()
    
    
