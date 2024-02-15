#!/bin/bash

echo "Téléchargement des fichiers de modèle..."
wget -O mlb_model.joblib https://github.com/walterwhites/Categorisez-automatiquement-des-questions/releases/download/v1.0.0/transformer_MultiLabelBinarizer.joblib
wget -O oneVsRestClassifier_mlb_model.joblib https://github.com/walterwhites/Categorisez-automatiquement-des-questions/releases/download/v1.0.0/model_supervised_OneVsRestClassifier_MultinomialNB.joblib

chmod +x download_models.sh
