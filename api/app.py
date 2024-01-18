from fastapi import FastAPI
import numpy as np
from joblib import load
from pydantic import BaseModel
from api.preprocessing import preprocess_text

app = FastAPI()

@app.on_event("startup")
def load_models():
    global combined_pipeline
    global mlb
    combined_pipeline = load('models/model_supervised_OneVsRestClassifier_MultinomialNB.joblib')
    mlb = load('models/model_supervised_MultinomialNB.joblib')

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

@app.post("/predict/", response_model=PredictionResponse)
def predict(question: str):
    prediction = combined_pipeline.predict([question])
    return PredictionResponse(prediction=prediction)