from pathlib import Path

import joblib
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

from preprocessing import clean_text


BASE_DIR = Path(__file__).resolve().parents[2]

DATASET_PATH = (
    BASE_DIR
    / "data"
    / "smsspam"
    / "SMSSpamCollection"
)

MODEL_DIR = Path(__file__).resolve().parent / "models"

MODEL_FILE = MODEL_DIR / "spam_model.joblib"


def load_dataset():
    df = pd.read_csv(
        DATASET_PATH,
        sep="\t",
        header=None,
        names=["label", "message"],
    )

    return df


def train():
    print("Cargando dataset...")

    df = load_dataset()

    df["message"] = df["message"].apply(clean_text)

    X = df["message"]
    y = df["label"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y,
    )

    pipeline = Pipeline(
        [
            ("tfidf", TfidfVectorizer()),
            ("classifier", MultinomialNB()),
        ]
    )

    print("Entrenando modelo...")

    pipeline.fit(X_train, y_train)

    predictions = pipeline.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)

    print(f"Accuracy: {accuracy:.4f}")

    MODEL_DIR.mkdir(exist_ok=True)

    joblib.dump(pipeline, MODEL_FILE)

    print(f"Modelo guardado en: {MODEL_FILE}")


if __name__ == "__main__":
    train()