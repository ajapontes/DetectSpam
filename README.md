# DetectSpam

## Spam Message Detection using Machine Learning

A web application that uses Natural Language Processing (NLP) and Machine Learning techniques to classify text messages as **SPAM** or **NOT SPAM**.

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

# Project Description

DetectSpam is a Machine Learning-based web application designed to identify spam messages through supervised learning techniques.

The application allows users to:

* Enter a text message.
* Receive a classification (SPAM or NOT SPAM).
* Obtain a confidence score.
* Receive a brief explanation of the prediction.

The solution combines a Machine Learning model, a REST API built with FastAPI, and a web interface developed using HTML, CSS, and JavaScript.

---

# Learning Objectives

The purpose of this project is to apply the complete Data Science lifecycle in a real-world spam detection scenario, including:

* Data acquisition.
* Exploratory Data Analysis (EDA).
* Data preprocessing.
* Feature engineering.
* Model training.
* Model evaluation.
* Deployment through a web application.

---

# Repository Structure

```text
DetectSpam/
│
├── app/
│   ├── main.py
│   ├── schemas.py
│   ├── services/
│   ├── ml/
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

Primary dataset used for model training.

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
python app/ml/train_model.py
```

The trained model will be generated automatically in:

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

# Current Results

Model:

* TF-IDF Vectorizer
* Multinomial Naive Bayes

Performance:

| Metric   | Value  |
| -------- | ------ |
| Accuracy | 96.05% |

---

# Future Work

* Precision, Recall and F1 Score evaluation.
* Confusion Matrix.
* Metrics Dashboard.
* Explainable AI (XAI).
* Transformer-based models.
* Adversarial spam detection.
* Integration with Large Language Models (LLMs).

---

# License

This repository was developed exclusively for educational and academic purposes.

Universidad Icesi
Master's Degree in Artificial Intelligence
Hacking IA
2026
