import re


def clean_text(text: str) -> str:
    """
    Clean and normalize a text message before feature extraction.

    This function applies basic preprocessing steps used by the
    machine learning pipeline:

    1. Validate that the input is a string.
    2. Convert text to lowercase.
    3. Remove punctuation and special characters.
    4. Replace multiple spaces with a single space.
    5. Remove leading and trailing spaces.

    Args:
        text (str): Original text message.

    Returns:
        str: Cleaned and normalized text message.
    """
    if not isinstance(text, str):
        return ""

    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()

    return text