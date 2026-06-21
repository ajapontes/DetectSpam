from pathlib import Path

import joblib
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

from app.ml.preprocessing import clean_text


# Project root directory
BASE_DIR = Path(__file__).resolve().parents[2]

# Path to the SMS Spam Collection dataset
DATASET_PATH = (
    BASE_DIR
    / "data"
    / "smsspam"
    / "SMSSpamCollection"
)

# Directory where the trained model will be stored
MODEL_DIR = Path(__file__).resolve().parent / "models"

# Full path of the serialized model file
MODEL_FILE = MODEL_DIR / "spam_model.joblib"


def load_dataset() -> pd.DataFrame:
    """
    Load the SMS Spam Collection dataset.

    The dataset contains two columns:
    - label: message category, either 'ham' or 'spam'
    - message: original SMS message text

    Returns:
        pd.DataFrame: Dataset loaded into a pandas DataFrame.
    """
    df = pd.read_csv(
        DATASET_PATH,
        sep="\t",
        header=None,
        names=["label", "message"],
    )

    # Ensure column names do not contain leading or trailing spaces
    df.columns = df.columns.str.strip()

    return df


def train() -> None:
    """
    Train and persist the spam detection model.

    This function performs the complete training workflow:
    1. Load the dataset.
    2. Clean the message text.
    3. Split the dataset into training and testing subsets.
    4. Build a pipeline with TF-IDF vectorization and Multinomial Naive Bayes.
    5. Train the model.
    6. Evaluate the model using accuracy.
    7. Save the trained pipeline as a joblib file.
    """
    print("Loading dataset...")

    df = load_dataset()

    # Apply the same text preprocessing used by the application
    df["message"] = df["message"].apply(clean_text)

    # Define input features and target variable
    X = df["message"]
    y = df["label"]

    # Split data into training and testing sets using stratification
    # to preserve the original class distribution.
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y,
    )

    # Build the machine learning pipeline.
    # TF-IDF converts text into numerical features.
    # Multinomial Naive Bayes performs the classification.
    pipeline = Pipeline(
        [
            ("tfidf", TfidfVectorizer()),
            ("classifier", MultinomialNB()),
        ]
    )

    print("Training model...")

    # Train the complete pipeline
    pipeline.fit(X_train, y_train)

    # Generate predictions on unseen test data
    predictions = pipeline.predict(X_test)

    # Evaluate model performance
    accuracy = accuracy_score(y_test, predictions)

    print(f"Accuracy: {accuracy:.4f}")

    # Create the model directory if it does not exist
    MODEL_DIR.mkdir(exist_ok=True)

    # Save the trained pipeline for later use by the FastAPI application
    joblib.dump(pipeline, MODEL_FILE)

    print(f"Model saved at: {MODEL_FILE}")


if __name__ == "__main__":
    train()