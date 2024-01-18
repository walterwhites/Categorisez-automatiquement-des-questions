# Cat-gorisez-automatiquement-des-questions

## récupérer les données du dataset
https://data.stackexchange.com/stackoverflow/query/edit/1810083
```SQL
SELECT TOP 50000 Title, Body, Tags, Score
FROM Posts
WHERE PostTypeId = 1 AND ViewCount >= 20 AND AnswerCount >= 1
AND Score >= 5 AND LEN(Tags) - LEN(REPLACE(Tags, '<','')) >= 5
```