from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model, authenticate, login as login_auth 
from django.contrib.auth.models import User
from django.conf import settings
from django.core.mail import send_mail
from Base.models import *
from .forms import *
import random
import string
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


def is_admin(user):
    return user.is_superuser

User = get_user_model()

class AdminUserCreateAPIView(APIView):
    def get(self, request):
        return render(request, 'admin_site/pages/createsuper.html')
    
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')

        if not username or not password or not email:
            return Response({'error': 'Tous les champs sont obligatoires.'}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username).exists():
            return Response({'error': 'Ce nom d\'utilisateur est déjà pris.'}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(email=email).exists():
            return Response({'error': 'Cet email est déjà utilisé.'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, password=password, email=email)
        user.is_staff = True  # Définir l'utilisateur comme administrateur
        user.save()

        return Response({'success': 'Compte administrateur créé avec succès.'}, status=status.HTTP_201_CREATED)




def login(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login_auth(request, user)
            return redirect('administration')
        else:
            return render(request, 'admin_site/pages/login.html', {'error_message': "Nom d'utilisateur ou mot de passe incorrect."})
    else:
        return render(request, 'admin_site/pages/login.html')


def request_password(request):
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "!@#$%^&*()."
    string = lower + upper + numbers + symbols
    length = 10

    generate_password = "".join(random.sample(string, length))
    return generate_password

class ResetPasswordAPIView(APIView):
    def get(self, request):
        return render(request, 'admin_site/pages/request_password.html')

    def post(self, request):
        email = request.data.get('email')

        if not email:
            return Response({'error': 'L\'email est obligatoire.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'error': 'Aucun utilisateur avec cet email.'}, status=status.HTTP_404_NOT_FOUND)

        # Générer un code de connexion aléatoire en utilisant la fonction request_password
        code = request_password(request)

        # Envoyer l'email avec le code de connexion
        subject = 'Réinitialisation de votre mot de passe'
        message = f'Votre code de connexion est : {code}'
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [user.email]

        send_mail(subject, message, from_email, recipient_list, fail_silently=False)

        # Enregistrer le code de connexion dans l'objet utilisateur
        user.password_reset_code = code
        user.save()

        return Response({'success': 'Un code de connexion a été envoyé à votre adresse email.'}, status=status.HTTP_200_OK)


class ConfirmResetPasswordAPIView(APIView):
    def get(self, request):
        return render(request, 'admin_site/pages/confirm_reset_password.html')

    def post(self, request):
        email = request.data.get('email')
        code = request.data.get('code')
        new_password = request.data.get('new_password')

        if not email or not code or not new_password:
            return Response({'error': 'Tous les champs sont obligatoires.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(email=email, password_reset_code=code)
        except User.DoesNotExist:
            return Response({'error': 'Code de réinitialisation invalide.'}, status=status.HTTP_400_BAD_REQUEST)

        user.password = make_password(new_password)
        user.password_reset_code = None
        user.save()

        return Response({'success': 'Votre mot de passe a été réinitialisé avec succès.'}, status=status.HTTP_200_OK)


@login_required(login_url='login')
def administration(request):
    context = {
        'carousel_count': Carrousel.objects.count(),
        'morceau_count': Morceau.objects.count(),
        'evenement_count': Evenement.objects.count(),
        'audio_count': Audio.objects.count(),
        'album_count': Album.objects.count(),
        'discographie_count': Discographie.objects.count(),
        'prochainconcert_count': Prochainconcert.objects.count(),
        'concert_count': Concert.objects.count(),
        'short_count': Short.objects.count(),
        'lifestyle_count': Lifestyle.objects.count(),
        'formation_count': Formation.objects.count(),
    }
    return render(request, 'admin_site/pages/index.html', context)



# Vues pour Carrousel
def CarrouselList(request):
    carrousels = Carrousel.objects.all()
    context = {'carrousels': carrousels}
    return render(request, 'admin_site/pages/carrousel/CarrouselList.html', context)

def CarrouselCreate(request):
    if request.method == 'POST':
        form = CarrouselForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('CarrouselList')
    else:
        form = CarrouselForm()
    context = {'form': form}
    return render(request, 'admin_site/pages/carrousel/CarrouselCreate.html', context)

def CarrouselUpdate(request, pk):
    carrousel = get_object_or_404(Carrousel, pk=pk)
    if request.method == 'POST':
        form = CarrouselForm(request.POST, request.FILES, instance=carrousel)
        if form.is_valid():
            form.save()
            return redirect('CarrouselList')
    else:
        form = CarrouselForm(instance=carrousel)
    context = {'form': form}
    return render(request, 'admin_site/pages/carrousel/CarrouselUpdate.html', context)

def CarrouselDelete(request, pk):
    carrousel = get_object_or_404(Carrousel, pk=pk)
    if request.method == 'POST':
        carrousel.delete()
        return redirect('CarrouselList')
    context = {'carrousel': carrousel}
    return render(request, 'admin_site/pages/carrousel/CarrouselDelete.html', context)

# Vues pour Morceau
def MorceauList(request):
    morceaux = Morceau.objects.all()
    context = {'morceaux': morceaux}
    return render(request, 'admin_site/pages/morceau/MorceauList.html', context)

def MorceauCreate(request):
    if request.method == 'POST':
        form = MorceauForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('MorceauList')
    else:
        form = MorceauForm()
    context = {'form': form}
    return render(request, 'admin_site/pages/morceau/MorceauCreate.html', context)

def MorceauUpdate(request, pk):
    morceau = get_object_or_404(Morceau, pk=pk)
    if request.method == 'POST':
        form = MorceauForm(request.POST, instance=morceau)
        if form.is_valid():
            form.save()
            return redirect('MorceauList')
    else:
        form = MorceauForm(instance=morceau)
    context = {'form': form}
    return render(request, 'admin_site/pages/morceau/MorceauUpdate.html', context)

def MorceauDelete(request, pk):
    morceau = get_object_or_404(Morceau, pk=pk)
    if request.method == 'POST':
        morceau.delete()
        return redirect('MorceauList')
    context = {'morceau': morceau}
    return render(request, 'admin_site/pages/morceau/MorceauDelete.html', context)
    
# Vues pour Evenement
def EvenementList(request):
    evenements = Evenement.objects.all()
    context = {'evenements': evenements}
    return render(request, 'admin_site/pages/evenement/EvenementList.html', context)

def EvenementCreate(request):
    if request.method == 'POST':
        form = EvenementForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('EvenementList')
    else:
        form = EvenementForm()
    context = {'form': form}
    return render(request, 'admin_site/pages/evenement/EvenementCreate.html', context)

def EvenementUpdate(request, pk):
    evenement = get_object_or_404(Evenement, pk=pk)
    if request.method == 'POST':
        form = EvenementForm(request.POST, request.FILES, instance=evenement)
        if form.is_valid():
            form.save()
            return redirect('EvenementList')
    else:
        form = EvenementForm(instance=evenement)
    context = {'form': form}
    return render(request, 'admin_site/pages/evenement/EvenementUpdate.html', context)

def EvenementDelete(request, pk):
    evenement = get_object_or_404(Evenement, pk=pk)
    if request.method == 'POST':
        evenement.delete()
        return redirect('EvenementList')
    context = {'evenement': evenement}
    return render(request, 'admin_site/pages/evenement/EvenementDelete.html', context)


# Vues pour Audio
def AudioList(request):
    audios = Audio.objects.all()
    context = {'audios': audios}
    return render(request, 'admin_site/pages/audio/AudioList.html', context)

def AudioCreate(request):
    if request.method == 'POST':
        form = AudioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('AudioList')
    else:
        form = AudioForm()
    context = {'form': form}
    return render(request, 'admin_site/pages/audio/AudioCreate.html', context)

def AudioUpdate(request, pk):
    audio = get_object_or_404(Audio, pk=pk)
    if request.method == 'POST':
        form = AudioForm(request.POST, request.FILES, instance=audio)
        if form.is_valid():
            form.save()
            return redirect('AudioList')
    else:
        form = AudioForm(instance=audio)
    context = {'form': form}
    return render(request, 'admin_site/pages/audio/AudioUpdate.html', context)

def AudioDelete(request, pk):
    audio = get_object_or_404(Audio, pk=pk)
    if request.method == 'POST':
        audio.delete()
        return redirect('AudioList')
    context = {'audio': audio}
    return render(request, 'admin_site/pages/audio/AudioDelete.html', context)

    
# Vues pour Album
def AlbumList(request):
    albums = Album.objects.all()
    context = {'albums': albums}
    return render(request, 'admin_site/pages/album/AlbumList.html', context)

def AlbumCreate(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('AlbumList')
    else:
        form = AlbumForm()
    context = {'form': form}
    return render(request, 'admin_site/pages/album/AlbumCreate.html', context)

def AlbumUpdate(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES, instance=album)
        if form.is_valid():
            form.save()
            return redirect('AlbumList')
    else:
        form = AlbumForm(instance=album)
    context = {'form': form}
    return render(request, 'admin_site/pages/album/AlbumUpdate.html', context)

def AlbumDelete(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        album.delete()
        return redirect('AlbumList')
    context = {'album': album}
    return render(request, 'admin_site/pages/album/AlbumDelete.html', context)
    
    
# Vues pour Discographie
def DiscographieList(request):
    discographies = Discographie.objects.all()
    context = {'discographies': discographies}
    return render(request, 'admin_site/pages/discographie/DiscographieList.html', context)

def DiscographieCreate(request):
    if request.method == 'POST':
        form = DiscographieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('DiscographieList')
    else:
        form = DiscographieForm()
    context = {'form': form}
    return render(request, 'admin_site/pages/discographie/DiscographieCreate.html', context)

def DiscographieUpdate(request, pk):
    discographie = get_object_or_404(Discographie, pk=pk)
    if request.method == 'POST':
        form = DiscographieForm(request.POST, request.FILES, instance=discographie)
        if form.is_valid():
            form.save()
            return redirect('DiscographieList')
    else:
        form = DiscographieForm(instance=discographie)
    context = {'form': form}
    return render(request, 'admin_site/pages/discographie/DiscographieUpdate.html', context)

def DiscographieDelete(request, pk):
    discographie = get_object_or_404(Discographie, pk=pk)
    if request.method == 'POST':
        discographie.delete()
        return redirect('DiscographieList')
    context = {'discographie': discographie}
    return render(request, 'admin_site/pages/discographie/DiscographieDelete.html', context)


# Vues pour Prochainconcert
def ProchainconcertList(request):
    prochainconcerts = Prochainconcert.objects.all()
    context = {'prochainconcerts': prochainconcerts}
    return render(request, 'admin_site/pages/concert/ProchainconcertList.html', context)

def ProchainconcertCreate(request):
    if request.method == 'POST':
        form = ProchainconcertForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ProchainconcertList')
    else:
        form = ProchainconcertForm()
    context = {'form': form}
    return render(request, 'admin_site/pages/concert/ProchainconcertCreate.html', context)

def ProchainconcertUpdate(request, pk):
    prochainconcert = get_object_or_404(Prochainconcert, pk=pk)
    if request.method == 'POST':
        form = ProchainconcertForm(request.POST, request.FILES, instance=prochainconcert)
        if form.is_valid():
            form.save()
            return redirect('ProchainconcertList')
    else:
        form = ProchainconcertForm(instance=prochainconcert)
    context = {'form': form}
    return render(request, 'admin_site/pages/concert/ProchainconcertUpdate.html', context)

def ProchainconcertDelete(request, pk):
    prochainconcert = get_object_or_404(Prochainconcert, pk=pk)
    if request.method == 'POST':
        prochainconcert.delete()
        return redirect('ProchainconcertList')
    context = {'prochainconcert': prochainconcert}
    return render(request, 'admin_site/pages/concert/ProchainconcertDelete.html', context)
    
    
# Vues pour Concert
def ConcertList(request):
    concerts = Concert.objects.all()
    context = {'concerts': concerts}
    return render(request, 'admin_site/pages/concert/ConcertList.html', context)

def ConcertCreate(request):
    if request.method == 'POST':
        form = ConcertForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ConcertList')
    else:
        form = ConcertForm()
    context = {'form': form}
    return render(request, 'admin_site/pages/concert/ConcertCreate.html', context)

def ConcertUpdate(request, pk):
    concert = get_object_or_404(Concert, pk=pk)
    if request.method == 'POST':
        form = ConcertForm(request.POST, request.FILES, instance=concert)
        if form.is_valid():
            form.save()
            return redirect('ConcertList')
    else:
        form = ConcertForm(instance=concert)
    context = {'form': form}
    return render(request, 'admin_site/pages/concert/ConcertUpdate.html', context)

def ConcertDelete(request, pk):
    concert = get_object_or_404(Concert, pk=pk)
    if request.method == 'POST':
        concert.delete()
        return redirect('ConcertList')
    context = {'concert': concert}
    return render(request, 'admin_site/pages/concert/ConcertDelete.html', context)


# Vues pour Short
@login_required(login_url='login')
def ShortList(request):
    shorts = Short.objects.all()
    return render(request, 'admin_site/pages/shorts/ShortList.html', {'shorts': shorts})

@login_required(login_url='login')
def ShortCreate(request):
    if request.method == 'POST':
        form = ShortForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ShortList')
    else:
        form = ShortForm()
    return render(request, 'admin_site/pages/shorts/ShortCreate.html', {'form': form})

@login_required(login_url='login')
def ShortUpdate(request, pk):
    short = get_object_or_404(Short, pk=pk)
    if request.method == 'POST':
        form = ShortForm(request.POST, request.FILES, instance=short)
        if form.is_valid():
            form.save()
            return redirect('ShortList')
    else:
        form = ShortForm(instance=short)
    return render(request, 'admin_site/pages/shorts/ShortUpdate.html', {'form': form})

@login_required(login_url='login')
def ShortDelete(request, pk):
    short = get_object_or_404(Short, pk=pk)
    if request.method == 'POST':
        short.delete()
        return redirect('ShortList')
    return render(request, 'admin_site/pages/shorts/ShortDelete.html', {'short': short})

# Vues pour Lifestyle
@login_required(login_url='login')
def LifestyleList(request):
    lifestyles = Lifestyle.objects.all()
    return render(request, 'admin_site/pages/lifestyle/LifestyleList.html', {'lifestyles': lifestyles})

@login_required(login_url='login')
def LifestyleCreate(request):
    if request.method == 'POST':
        form = LifestyleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('LifestyleList')
    else:
        form = LifestyleForm()
    return render(request, 'admin_site/pages/lifestyle/LifestyleCreate.html', {'form': form})

@login_required(login_url='login')
def LifestyleUpdate(request, pk):
    lifestyle = get_object_or_404(Lifestyle, pk=pk)
    if request.method == 'POST':
        form = LifestyleForm(request.POST, request.FILES, instance=lifestyle)
        if form.is_valid():
            form.save()
            return redirect('LifestyleList')
    else:
        form = LifestyleForm(instance=lifestyle)
    return render(request, 'admin_site/pages/lifestyle/LifestyleUpdate.html', {'form': form})

@login_required(login_url='login')
def LifestyleDelete(request, pk):
    lifestyle = get_object_or_404(Lifestyle, pk=pk)
    if request.method == 'POST':
        lifestyle.delete()
        return redirect('LifestyleList')
    return render(request, 'admin_site/pages/lifestyle/LifestyleDelete.html', {'lifestyle': lifestyle})

# Vues pour Formation
@login_required(login_url='login')
def FormationList(request):
    formations = Formation.objects.all()
    return render(request, 'admin_site/pages/formation/FormationList.html', {'formations': formations})

@login_required(login_url='login')
def FormationCreate(request):
    if request.method == 'POST':
        form = FormationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('FormationList')
    else:
        form = FormationForm()
    return render(request, 'admin_site/pages/formation/FormationCreate.html', {'form': form})

@login_required(login_url='login')
def FormationUpdate(request, pk):
    formation = get_object_or_404(Formation, pk=pk)
    if request.method == 'POST':
        form = FormationForm(request.POST, request.FILES, instance=formation)
        if form.is_valid():
            form.save()
            return redirect('FormationList')
    else:
        form = FormationForm(instance=formation)
    return render(request, 'admin_site/pages/formation/FormationUpdate.html', {'form': form})

@login_required(login_url='login')
def FormationDelete(request, pk):
    formation = get_object_or_404(Formation, pk=pk)
    if request.method == 'POST':
        formation.delete()
        return redirect('FormationList')
    return render(request, 'admin_site/pages/formation/FormationDelete.html', {'formation': formation})