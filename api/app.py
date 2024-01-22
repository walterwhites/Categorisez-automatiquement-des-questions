from fastapi import FastAPI
import numpy as np
import requests
from joblib import load
from pydantic import BaseModel
from api.preprocessing import preprocess_text
import streamlit as st
import httpx

app = FastAPI()
mlb_model_url = 'https://github.com/walterwhites/Categorisez-automatiquement-des-questions/releases/download/v1.0.0/model_supervised_MultinomialNB.joblib'
oneVsRestClassifier_mlb_model_url = 'https://github.com/walterwhites/Categorisez-automatiquement-des-questions/releases/download/v1.0.0/model_supervised_OneVsRestClassifier_MultinomialNB.joblib'

combined_pipeline = None
mlb = None

api_url = "https://share.streamlit.io/votre-nom/nom-de-votre-application/models/supervised/predict/"

def download_file(url, filename):
    response = requests.get(url)
    response.raise_for_status()
    with open(filename, 'wb') as f:
        f.write(response.content)
@app.on_event("startup")
def load_models():
    global combined_pipeline
    global mlb

    download_file(mlb_model_url, "mlb_model.joblib")
    download_file(oneVsRestClassifier_mlb_model_url, "oneVsRestClassifier_mlb_model.joblib")
    combined_pipeline = load('oneVsRestClassifier_mlb_model.joblib')
    mlb = load('mlb_model.joblib')

class PredictionResponse(BaseModel):
    prediction: str

@app.post("/models/supervised/predict/")
def supervised_predict(title: str, body: str):
    content = title + ' ' + body
    processed_question = preprocess_text(content)
    content_as_array = [title, body]
    print(content_as_array)
    predictions_proba_combined = combined_pipeline.predict_proba(content_as_array)

    n_top_classes = 5

    # itérer sur chaque prédiction
    for i, question in enumerate(processed_question):
        top_classes_indices = predictions_proba_combined.argsort(axis=1)[:, -n_top_classes:][i]
        top_classes_probabilities = predictions_proba_combined[i, top_classes_indices]

        # Tri des classes et des probabilités par ordre décroissant de probabilité
        sorted_indices = np.argsort(top_classes_probabilities)[::-1]
        top_tags_combined_sorted = mlb.classes_[top_classes_indices[sorted_indices]]
        top_classes_probabilities_sorted = top_classes_probabilities[sorted_indices]

        print(f"Tags associés pour la question '{question}':", list(zip(top_tags_combined_sorted, top_classes_probabilities_sorted)))
        print("\n")

    return {"prediction":  list(zip(top_tags_combined_sorted, top_classes_probabilities_sorted))}
def main():
    st.title("Votre Application Streamlit")
    title = st.text_input("Titre")
    body = st.text_area("Corps")

    if st.button("Prédire"):
        with st.spinner("En cours de prédiction..."):
            data = {"title": title, "body": body}
            response = requests.post(api_url, json=data)
            prediction = response.json()
            st.write("Prédiction:", prediction)
