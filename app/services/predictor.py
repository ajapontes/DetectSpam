from pathlib import Path

import joblib

from app.ml.preprocessing import clean_text


MODEL_PATH = (
    Path(__file__).resolve().parents[1]
    / "ml"
    / "models"
    / "spam_model.joblib"
)


class SpamPredictor:
    def __init__(self):
        self.model = joblib.load(MODEL_PATH)

    def predict(self, text: str) -> dict:
        cleaned_text = clean_text(text)

        prediction = self.model.predict([cleaned_text])[0]
        probabilities = self.model.predict_proba([cleaned_text])[0]

        classes = list(self.model.classes_)
        prediction_index = classes.index(prediction)
        confidence = float(probabilities[prediction_index])

        explanation = (
            "El mensaje contiene patrones frecuentes en mensajes spam, como promociones, premios, urgencia o llamadas a la acción."
            if prediction == "spam"
            else "El mensaje no presenta suficientes señales típicas de spam según el modelo entrenado."
        )

        return {
            "prediction": prediction,
            "confidence": round(confidence, 4),
            "message": text,
            "explanation": explanation,
        }

predictor = SpamPredictor()

