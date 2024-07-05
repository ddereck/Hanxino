from django.forms import ModelForm
from Base.models import Carrousel, Morceau, Evenement, Audio, Album, Discographie, Prochainconcert, Concert, Short, Lifestyle, Formation

class CarrouselForm(ModelForm):
    class Meta:
        model = Carrousel
        fields = ['image']

class MorceauForm(ModelForm):
    class Meta:
        model = Morceau
        fields = ['titre', 'description', 'video']

class EvenementForm(ModelForm):
    class Meta:
        model = Evenement
        fields = ['image', 'cover', 'titre', 'date', 'lieu']

class AudioForm(ModelForm):
    class Meta:
        model = Audio
        fields = ['titre', 'audio']

class AlbumForm(ModelForm):
    class Meta:
        model = Album
        fields = ['image']

class DiscographieForm(ModelForm):
    class Meta:
        model = Discographie
        fields = ['image', 'detail', 'titre', 'prix', 'link']

class ProchainconcertForm(ModelForm):
    class Meta:
        model = Prochainconcert
        fields = ['image', 'date', 'titre', 'prix']

class ConcertForm(ModelForm):
    class Meta:
        model = Concert
        fields = ['image', 'date', 'titre', 'lieu', 'heure', 'description', 'prix']
        
        
class ShortForm(ModelForm):
    class Meta:
        model = Short
        fields = ['video']
        
class LifestyleForm(ModelForm):
    class Meta:
        model = Lifestyle
        fields = ['photo']
        
class FormationForm(ModelForm):
    class Meta:
        model = Formation
        fields = ['video']
        