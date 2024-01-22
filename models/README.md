# Cat-gorisez-automatiquement-des-questions

## Récupérer les données du dataset
https://data.stackexchange.com/stackoverflow/query/edit/1810083
```SQL
SELECT TOP 50000 Title, Body, Tags, Score
FROM Posts
WHERE PostTypeId = 1 AND ViewCount >= 20 AND AnswerCount >= 1
AND Score >= 5 AND LEN(Tags) - LEN(REPLACE(Tags, '<','')) >= 5
```

## mlflow UI
Dans la racine du projet lancez la commande
```
mlflow ui
```

## API en local
Dans la racine du projet lancez la commande
```
 uvicorn api.app:app --reload
```

Ensuite, naviguez vers http://localhost:8000/docs


## Virtual env
Création de l'env virtuel
```
python -m venv my_env 
```

Pour activer l'env virtuel
```
source my_env/bin/activate
```
