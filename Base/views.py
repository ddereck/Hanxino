from django.urls import path
from .models import *
from datetime import datetime
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.http import HttpResponse, JsonResponse
import qrcode
from django.conf import settings
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect, render



User = get_user_model()

def countdown_view(request):
    # Récupérer la prochaine date de concert à partir de la base de données
    prochain_concert = Prochainconcert.objects.first()
    return render(request, 'countdown.html', {'prochain_concert': prochain_concert,})

def home(request):
    carrousels = Carrousel.objects.all()
    morceaus = Morceau.objects.all() 
    evenements = Evenement.objects.all()
    artistes = Artiste.objects.all()
    audios =Audio.objects.all()
    youtubevds = Youtubevd.objects.all()
    # Récupérer la prochaine date de concert à partir de la base de données
    prochain_concert = Prochainconcert.objects.first()
    prochainconcert = Prochainconcert.objects.all()
    context = {'carrousels': carrousels, 'morceaus': morceaus, 'evenements': evenements, 'artistes': artistes,
               'audios': audios, 'youtubevds': youtubevds, 'prochainconcert':prochainconcert, 'prochain_concert': prochain_concert,} 
    return render(request, 'pages/index.html', context)


def join(request):
    if request.method == 'POST':
        nom = request.POST.get('nom', '')
        objet = request.POST.get('objet', '')
        message = request.POST.get('message', '')

        # Envoyer l'e-mail
        send_mail(
            objet,
            message,
            'noreply@example.com', 
            ['itgillo60@gmail.com'],  
        )

        # Message de confirmation après l'envoi du message
        return HttpResponse("Message envoyé avec succès!")
    else:
        contacts = Contact.objects.all()
        context ={'contacts':contacts,}
        return render(request, 'pages/contact.html', context)

def discography(request):
    discographies = Discographie.objects.all()
    context ={'discographies':discographies,}
    return render(request, 'pages/discography.html', context)

def tours(request):
    # Récupérer la prochaine date de concert à partir de la base de données
    prochain_concert = Prochainconcert.objects.first()
    prochainconcert = Prochainconcert.objects.all()
    concerts = Concert.objects.all()
    context ={'concerts':concerts, 'prochainconcert':prochainconcert, 'prochain_concert': prochain_concert,}
    return render(request, 'pages/tours.html', context)

def videos(request):
    resumeconcert1s = ResumeConcert1.objects.all()
    resumeconcerts = ResumeConcert.objects.all()
    context ={'resumeconcert1s':resumeconcert1s, 'resumeconcerts':resumeconcerts}
    return render(request, 'pages/videos.html', context)

def about(request):
    discotheques = Album.objects.all()
    context ={'discotheques':discotheques,}
    return render(request, 'pages/about.html', context)


def univers(request):
    context = {
        'shorts': Short.objects.all(),
        'lifestyles': Lifestyle.objects.all(),
        'formations': Formation.objects.all(),
    }
    return render(request, 'pages/univers.html', context)



@csrf_exempt
def kkiapay_callback(request):
    if request.method == 'POST':
        # Récupérez les données de paiement du callback
        nom_evenement = request.POST.get('event-title')
        nom_prenom = request.POST.get('prenom')
        montant_paye = request.POST.get('montant')
        email_acheteur = request.POST.get('email')
        date_paiement = timezone.now()


        # Créer ou mettre à jour une entrée de paiement dans la base de données
        payment, created = Payment.objects.get_or_create(
            nom_evenement=nom_evenement,
            nom_prenom=nom_prenom,
            montant_paye=montant_paye,
            email_acheteur=email_acheteur,
            defaults={'date_paiement': date_paiement}
        )

        # Si le paiement a été créé, cela signifie qu'il n'existait pas déjà dans la base de données
        if created:
            print("Nouveau paiement créé :", payment)
        else:
            print("Paiement existant mis à jour :", payment)


        # Vérifiez si l'email de l'acheteur est disponible
        if email_acheteur:
            # Générez le contenu pour le code QR
            payment_info = "Nom: {}\nMontant: {}\nÉvénement: {}\nDate de paiement: {}".format(nom_prenom, montant_paye, nom_evenement,  timezone.now())

            # Générez et enregistrez le code QR
            qr = qrcode.make(payment_info)
            qr_path = "QRCode.png"
            qr.save(qr_path)

            # Envoyez un email avec les informations de paiement et le code QR en pièce jointe
            send_mail(
                'Informations de paiement',
                'Voici les détails de votre paiement : Nom: {}, Montant: {}, Événement: {}, Date de paiement: {}'.format(nom_prenom, montant_paye, nom_evenement, timezone.now()),
                settings.EMAIL_HOST_USER,
                [email_acheteur],  # Utilisez l'email de l'acheteur comme destinataire de l'email
                fail_silently=False,
                html_message='<p>Voici les détails de votre paiement :</p><p>Nom: {}</p><p>Montant: {}</p><p>Événement: {}</p><p>Date de paiement: {}</p>'.format(nom_prenom, montant_paye, nom_evenement, timezone.now()),
                attachment=qr_path
            )


            return redirect('success')
        else:
            return HttpResponse("Email de l'acheteur non disponible", status=400)
    else:
        return HttpResponse(status=405)
    

def success_view(request):
    return render(request, 'success.html')
