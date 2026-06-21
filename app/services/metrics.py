"""
Model evaluation metrics for DetectSpam.

These metrics were obtained from the Data Science notebook using the
SMS Spam Collection test dataset.
"""


def get_model_metrics() -> dict:
    """
    Return the current model evaluation metrics.

    Returns:
        dict: Model performance metrics and confusion matrix values.
    """
    return {
        "model": "TF-IDF + Multinomial Naive Bayes",
        "accuracy": 0.9605,
        "precision": 1.0000,
        "recall": 0.7047,
        "f1_score": 0.8268,
        "confusion_matrix": {
            "true_negatives": 966,
            "false_positives": 0,
            "false_negatives": 44,
            "true_positives": 105,
        },
    }