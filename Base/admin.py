from django.contrib import admin
from .models import *

@admin.register(Carrousel)
class CarrouselAdmin(admin.ModelAdmin):
    list_display = ('id',)
    
@admin.register(Morceau)
class MorceauAdmin(admin.ModelAdmin):
    list_display = ('titre',)
    
@admin.register(Evenement)
class EvenementAdmin(admin.ModelAdmin):
    list_display = ('titre',)

@admin.register(Artiste)
class ArtisteAdmin(admin.ModelAdmin):
    list_display = ('nom',)

@admin.register(Audio)
class AudioAdmin(admin.ModelAdmin):
    list_display = ('titre',)

@admin.register(Youtubevd)
class YoutubevdAdmin(admin.ModelAdmin):
    pass

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    pass

@admin.register(Discographie)
class DiscographieAdmin(admin.ModelAdmin):
    pass

@admin.register(Concert)
class ConcertAdmin(admin.ModelAdmin):
    list_display = ('titre', 'date', 'lieu', 'heure')
    
@admin.register(Prochainconcert)
class ProchainconcertAdmin(admin.ModelAdmin):
    list_display = ('titre', 'date')

@admin.register(ResumeConcert1)
class ResumeConcert1Admin(admin.ModelAdmin):
    list_display = ('date', 'description')

@admin.register(ResumeConcert)
class ResumeConcertAdmin(admin.ModelAdmin):
    list_display = ('date', 'description')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('ville', 'tel1', 'tel2')
    
@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('nom_prenom', 'nom_evenement', 'date_paiement')    

@admin.register(Short)
class ShortAdmin(admin.ModelAdmin):
    pass    

@admin.register(Lifestyle)
class LifestyleAdmin(admin.ModelAdmin):
    pass

@admin.register(Formation)
class FormationAdmin(admin.ModelAdmin):
    pass