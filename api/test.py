import requests

api_url = "https://project5-f3fbec0b0078.herokuapp.com/models/supervised/predict/"

# Données de test
data = {
    "title": "Titre de test",
    "body": "Corps de test"
}

# Envoi de la requête POST
response = requests.post(api_url, json=data)

print("response")
print(response.status_code)
# Traitement de la réponse
if response.status_code == 200:
    prediction = response.json()
    print("Prédiction:", prediction)
else:
    print("Erreur lors de la requête :", response.status_code)
    print(response.text)
