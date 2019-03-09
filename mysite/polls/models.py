from django.db import models



# Create your models here.
class Equipe(models.Model):
    id = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=250)
    drapeau = models.CharField(max_length=250)


    def __str__(self):
        return self.nom + ' - ' + self.drapeau

class Joueur(models.Model):
    id = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=250)
    present = models.BooleanField(default= False)
    equipe_id = models.ForeignKey(Equipe, on_delete=models.CASCADE)


    def __str__(self):
        return self.nom