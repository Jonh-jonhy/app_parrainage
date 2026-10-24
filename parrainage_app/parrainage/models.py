from django.db import models

class Parrain(models.Model):
    nom = models.CharField(max_length=20)
    prenom = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.nom} - {self.prenom}"
    


class Filleul(models.Model):
    nom = models.CharField(max_length=20)
    prenom = models.CharField(max_length=30)
    parrain = models.ForeignKey(Parrain, on_delete=models.SET_NULL, blank=True, null=True, related_name="filleuls")

    def __str__(self):
        return f"{self.nom} - {self.prenom}"