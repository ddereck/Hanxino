from django.contrib.auth.models import AbstractUser
from django.db import models


class Carrousel(models.Model):
    image = models.ImageField(upload_to='carrousels/')
    
    
class Morceau(models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField()
    video = models.URLField()

    def __str__(self):
        return self.titre
    
     
class Evenement(models.Model):
    image = models.ImageField(upload_to='evenements/')
    cover = models.ImageField(upload_to='affiches/')
    titre = models.CharField(max_length=100)
    date = models.DateField()
    lieu = models.CharField(max_length=100)


class Artiste(models.Model):
    image = models.ImageField(upload_to='artiste/')
    nom = models.CharField(max_length=100)
    description = models.TextField()


class Audio(models.Model):
    titre = models.CharField(max_length=100)
    audio = models.FileField(upload_to='audios/')


class Youtubevd(models.Model):
    photo = models.ImageField(upload_to='youtubevd/')
    description = models.TextField()
    video = models.URLField()


class Album(models.Model):
    image = models.ImageField(upload_to='discotheques/')


class Discographie(models.Model):
    image = models.ImageField(upload_to='albums/')
    detail = models.ImageField(upload_to='albums/')
    titre = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=8, decimal_places=0)
    link = models.URLField()

class Concert(models.Model):
    image = models.ImageField(upload_to='concerts/')
    date = models.DateField()
    titre = models.CharField(max_length=100)
    lieu = models.CharField(max_length=100)
    heure = models.TimeField()
    description = models.TextField()
    prix = models.DecimalField(max_digits=8, decimal_places=0)

class Prochainconcert(models.Model):
    image = models.ImageField(upload_to='concerts/')
    date = models.DateTimeField()
    titre = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=8, decimal_places=0)

class ResumeConcert1(models.Model):
    video = models.URLField()
    image = models.ImageField(upload_to='mediaconcerts/')
    description = models.TextField()
    duree = models.DurationField()
    date = models.DateField()
    
    
class ResumeConcert(models.Model):
    video = models.URLField()
    image = models.ImageField(upload_to='mediaconcerts/')
    description = models.TextField()
    duree = models.DurationField()
    date = models.DateField()
 
class Contact(models.Model):
    ville = models.TextField(max_length=12)
    quartier = models.TextField(max_length=15)
    tel1 =  models.CharField(max_length=12)
    tel2 =  models.CharField(max_length=12)
    mail = models.EmailField()
    remail = models.EmailField()
    
    
    
class Payment(models.Model):
    nom_evenement = models.CharField(max_length=100)
    nom_prenom = models.CharField(max_length=100)
    montant_paye = models.DecimalField(max_digits=10, decimal_places=2)
    email_acheteur = models.EmailField() 
    date_paiement = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom_prenom} - {self.nom_evenement} - {self.montant_paye} - {self.date_paiement}"


class Short(models.Model):
    video = models.FileField(upload_to='shorts/')
    

class Lifestyle(models.Model):
    photo = models.ImageField(upload_to='lifestyles/')
    
    
class Formation(models.Model):
    video = models.FileField(upload_to='formations/')