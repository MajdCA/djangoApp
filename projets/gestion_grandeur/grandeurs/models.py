from django.db import models

# Create your models here.

class Grandeur(models.Model) :
    #id= models.AutoField
    nom = models.CharField(max_length=50)
    unite = models.CharField(max_length=20)
    valeurMin= models.FloatField()
    valeurMax= models.FloatField()

    def __str__(self) -> str:
        return f"Grandeur: {self.nom} unite: {self.unite} valeurs entre {self.valeurMin} et  {self.valeurMax} "


class Mesure(models.Model):
    valeur = models.FloatField()
    datePrise=models.DateTimeField()
    Grandeur=models.ForeignKey('Grandeur', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"Mesure: {self.valeur} at {self.datePrise}"
