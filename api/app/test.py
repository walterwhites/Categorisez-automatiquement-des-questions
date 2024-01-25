import requests

api_url = "https://project5-f3fbec0b0078.herokuapp.com/models/supervised/predict/"

data = {
    "title": "Titre de test",
    "body": "Corps de test"
}

headers = {
    "Accept": "application/json",
    "Referer": "https://project5-f3fbec0b0078.herokuapp.com/docs"
}

response = requests.post(api_url, json=data, headers=headers)

if response.status_code == 200:
    prediction = response.json()
    print("Prédiction:", prediction)
else:
    print("Erreur lors de la requête :", response.status_code)
    print(response.text)
