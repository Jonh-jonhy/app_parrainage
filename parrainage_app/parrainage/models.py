from django.db import models

class Parrain(models.Model):
    nom = models.CharField(max_length=20)
    prenom = models.CharField(max_length=30)



class Filleul(models.Model):
    nom = models.CharField(max_length=20)
    prenom = models.CharField(max_length=30)
    parrain = models.ForeignKey(Parrain, on_delete=models.SET_NULL, blank=True, null=True)