from pathlib import Path

import joblib

from app.ml.preprocessing import clean_text


# Path to the trained machine learning model
MODEL_PATH = (
    Path(__file__).resolve().parents[1]
    / "ml"
    / "models"
    / "spam_model.joblib"
)


class SpamPredictor:
    """
    Wrapper class responsible for loading the trained model
    and generating predictions for incoming messages.
    """

    def __init__(self):
        """
        Load the trained machine learning model into memory.
        """
        self.model = joblib.load(MODEL_PATH)

    def predict(self, text: str) -> dict:
        """
        Predict whether a message is spam or ham.

        Args:
            text (str):
                Original message provided by the user.

        Returns:
            dict:
                Prediction result including:
                - prediction
                - confidence
                - original message
                - explanation
        """

        # Apply the same preprocessing pipeline used during training
        cleaned_text = clean_text(text)

        # Generate prediction
        prediction = self.model.predict([cleaned_text])[0]

        # Calculate prediction confidence
        probabilities = self.model.predict_proba([cleaned_text])[0]

        classes = list(self.model.classes_)
        prediction_index = classes.index(prediction)
        confidence = float(probabilities[prediction_index])

        # Generate a human-readable explanation
        explanation = (
            "The message contains patterns commonly associated with spam, such as promotions, prizes, urgency, or calls to action."
            if prediction == "spam"
            else "The message does not contain enough characteristics typically associated with spam according to the trained model."
        )

        return {
            "prediction": prediction,
            "confidence": round(confidence, 4),
            "message": text,
            "explanation": explanation,
        }


# Singleton instance used throughout the application
predictor = SpamPredictor()