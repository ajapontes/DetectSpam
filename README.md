# DetectSpam

## Spam Message Detection using Machine Learning

DetectSpam is a web application that uses Natural Language Processing (NLP) and Machine Learning techniques to classify text messages as **SPAM** or **HAM (Not Spam)**.

The project combines a complete Data Science workflow, a Machine Learning model, a REST API built with FastAPI, and a web interface developed using HTML, CSS, and JavaScript.

---

# Academic Context

This project was developed as part of the **Master's Degree in Artificial Intelligence** at **Universidad Icesi**, within the course:

**Hackeando la IA**

Course Instructor:

**Professor Christian Urcuqui**

Year:

**2026**

---

# Project Team

* Alfredo Aponte
* Arlex Pino

---

# Project Objectives

The primary objective of this project is to design, implement, and evaluate a Machine Learning-based spam detection system capable of automatically classifying SMS messages.

The project applies the complete Data Science lifecycle, including:

* Data acquisition
* Exploratory Data Analysis (EDA)
* Text preprocessing
* Feature engineering
* Model training
* Model evaluation
* Deployment through a web application

---

# Solution Architecture

The solution consists of four main components:

## Data Layer

Datasets used for training and experimentation:

* SMS Spam Collection Dataset
* Spambase Dataset

## Machine Learning Layer

* Text Preprocessing
* TF-IDF Vectorization
* Multinomial Naive Bayes Classifier

## Backend Layer

* FastAPI
* REST API Endpoints
* Prediction Service

## Frontend Layer

* HTML5
* CSS3
* JavaScript

---

# Repository Structure

```text
DetectSpam/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── schemas.py
│   │
│   ├── services/
│   │   └── predictor.py
│   │
│   ├── ml/
│   │   ├── __init__.py
│   │   ├── preprocessing.py
│   │   ├── train_model.py
│   │   └── models/
│   │
│   ├── templates/
│   └── static/
│
├── data/
│   ├── smsspam/
│   └── spambase/
│
├── notebook/
│   └── DetectSpam_DataScience_Process.ipynb
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Datasets

## SMS Spam Collection Dataset

Primary dataset used for training.

Characteristics:

* 5,574 SMS messages
* Binary classification:

  * ham
  * spam

Source:

https://archive.ics.uci.edu/dataset/228/sms+spam+collection

---

## Spambase Dataset

Secondary dataset included for future experimentation and comparative analysis.

Characteristics:

* 4,601 email messages
* 57 numerical features
* Binary spam classification

Source:

https://archive.ics.uci.edu/dataset/94/spambase

---

# Data Science Notebook

The complete Data Science process is documented in:

```text
notebook/DetectSpam_DataScience_Process.ipynb
```

The notebook includes:

* Data loading
* Exploratory Data Analysis (EDA)
* Class distribution analysis
* Message length analysis
* Frequent word analysis
* Text preprocessing
* TF-IDF feature engineering
* Train/Test split
* Model training
* Model evaluation
* Confusion matrix analysis
* Classification report
* Prediction examples
* Conclusions and future work

---

# Technologies

## Backend

* Python 3.11
* FastAPI
* Uvicorn

## Machine Learning

* Scikit-Learn
* Pandas
* NumPy
* Joblib

## Data Science

* Jupyter Notebook
* Matplotlib

## Frontend

* HTML5
* CSS3
* JavaScript

---

# Installation

## Create Virtual Environment

```bash
python -m venv .venv
```

## Activate Environment

Windows:

```bash
.venv\Scripts\activate
```

Linux / macOS:

```bash
source .venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Training the Model

```bash
python -m app.ml.train_model
```

The trained model will be stored in:

```text
app/ml/models/spam_model.joblib
```

---

# Running the Application

```bash
uvicorn app.main:app --reload
```

Application URL:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

---

# Model Performance

Model:

* TF-IDF Vectorizer
* Multinomial Naive Bayes

Evaluation Results:

| Metric    | Value   |
| --------- | ------- |
| Accuracy  | 96.05%  |
| Precision | 100.00% |
| Recall    | 70.47%  |
| F1 Score  | 82.68%  |

---

# Confusion Matrix

| Actual / Predicted | Ham | Spam |
| ------------------ | --- | ---- |
| Ham                | 966 | 0    |
| Spam               | 44  | 105  |

Observations:

* No false positives were generated.
* The classifier is highly conservative when labeling spam messages.
* Some spam messages remain undetected, impacting recall.

---

# Future Work

Potential future improvements include:

* Improving recall while preserving high precision.
* Evaluating Logistic Regression and Random Forest models.
* Experimenting with Deep Learning and Transformer-based approaches.
* Implementing Explainable AI (XAI) techniques.
* Creating a metrics dashboard.
* Supporting continuous model retraining.
* Exploring adversarial spam detection scenarios.

---

# License

This repository was developed exclusively for educational and academic purposes.

Universidad Icesi

Master's Degree in Artificial Intelligence

Hackeando la IA

2026
