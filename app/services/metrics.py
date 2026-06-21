from pathlib import Path
import json


# Path to the generated metrics file
METRICS_FILE = (
    Path(__file__).resolve().parents[1]
    / "ml"
    / "models"
    / "metrics.json"
)


def get_model_metrics() -> dict:
    """
    Load model evaluation metrics from the generated JSON file.

    The metrics file is created during model training by running:
    python -m app.ml.train_model

    Returns:
        dict: Model evaluation metrics.

    Raises:
        FileNotFoundError: If metrics.json has not been generated yet.
    """
    if not METRICS_FILE.exists():
        return {
            "status": "not_available",
            "message": (
                "Metrics file was not found. "
                "Run 'python -m app.ml.train_model' to generate it."
            ),
        }

    with open(METRICS_FILE, "r", encoding="utf-8") as file:
        return json.load(file)