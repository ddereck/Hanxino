import requests

# URL de l'API de paiement
url = 'http://127.0.0.1:8000/api/payments/'

# Données de paiement à envoyer
data = {
    'nom_evenement': 'Mariage 3.0',
    'nom_prenom': 'Onésime Sergent',
    'montant_paye': '10000',  
    'email_acheteur': 'sovionesime@gmail.com',
    'date_paiement': '2024/04/30',
    # Ajoutez d'autres champs de données si nécessaire
}

# Envoi de la requête POST à l'API de paiement
response = requests.post(url, data=data)

# Vérification de la réponse de la requête
if response.status_code == 200:
    print('Paiement effectué avec succès!')
else:
    print('Une erreur s\'est produite lors du paiement:', response.text)
