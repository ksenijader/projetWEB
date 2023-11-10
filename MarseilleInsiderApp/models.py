from django.db import models

# Create your models here.
class Loisir(models.Model):
    saison= models.CharField(max_length=255,verbose_name="Saison du loisir")
    nom=models.CharField(max_length=255, verbose_name="Nom du loisir")
    adresse=models.CharField(max_length=255, verbose_name="Adresse du loisir")
