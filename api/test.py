import requests

api_url = "https://categorisez-automatiquement-des-questions-5k9epyoc4gkbruabktk8.streamlit.app/models/supervised/predict/"

# Données de test
data = {
    "title": "Titre de test",
    "body": "Corps de test"
}

# Envoi de la requête POST
response = requests.post(api_url, json=data)

# Traitement de la réponse
if response.status_code == 200:
    prediction = response.json()
    print("Prédiction:", prediction)
else:
    print("Erreur lors de la requête :", response.status_code)
    print(response.text)