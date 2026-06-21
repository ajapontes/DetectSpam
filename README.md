# DetectSpam

> Detección Inteligente de Mensajes SPAM mediante Machine Learning

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.116-green)
![ScikitLearn](https://img.shields.io/badge/Scikit--Learn-ML-orange)
![Status](https://img.shields.io/badge/Status-MVP-success)

---

# Contexto Académico

Este proyecto fue desarrollado como parte de la **Maestría en Inteligencia Artificial de la Universidad Icesi** dentro de la asignatura:

## Hackeando la IA

Autores:

* Alfredo Aponte
* Arlex Pino

Año:

* 2026

---

# Descripción

DetectSpam es una aplicación web desarrollada en Python que utiliza técnicas de Procesamiento de Lenguaje Natural (NLP) y Machine Learning para clasificar mensajes como:

* SPAM
* NO SPAM

La solución permite que un usuario ingrese un mensaje de texto y obtenga:

* Clasificación automática
* Nivel de confianza
* Explicación básica del resultado

---

# Objetivo General

Diseñar e implementar una solución de Inteligencia Artificial capaz de identificar mensajes SPAM mediante técnicas de aprendizaje supervisado.

---

# Objetivos Específicos

* Construir un pipeline de procesamiento de texto.
* Implementar técnicas de limpieza y normalización.
* Entrenar un modelo de clasificación supervisada.
* Exponer el modelo mediante una API REST.
* Desarrollar una interfaz web para la interacción con usuarios.
* Evaluar el desempeño del modelo mediante métricas estándar.

---

# Arquitectura de la Solución

```text
┌─────────────┐
│   Usuario   │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ Frontend UI │
│ HTML/CSS/JS │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   FastAPI   │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ NLP Pipeline│
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ Modelo ML   │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ Predicción  │
└─────────────┘
```

---

# Tecnologías Utilizadas

## Backend

* Python 3.11
* FastAPI
* Uvicorn

## Machine Learning

* Scikit-Learn
* Pandas
* NumPy
* Joblib

## NLP

* Regex
* TF-IDF Vectorizer

## Frontend

* HTML5
* CSS3
* JavaScript

---

# Dataset Utilizados

## SMS Spam Collection

Dataset principal utilizado para entrenamiento.

Características:

* 5.574 mensajes SMS
* Clasificación binaria:

  * ham
  * spam

Fuente:

https://archive.ics.uci.edu/dataset/228/sms+spam+collection

---

## Spambase

Dataset complementario incluido para futuras investigaciones y comparaciones.

Características:

* 4.601 correos electrónicos
* 57 variables numéricas
* Clasificación binaria spam/no spam

Fuente:

https://archive.ics.uci.edu/dataset/94/spambase

---

# Pipeline de Machine Learning

## Preprocesamiento

Se realizan las siguientes transformaciones:

1. Conversión a minúsculas
2. Eliminación de caracteres especiales
3. Eliminación de espacios redundantes

Ejemplo:

Entrada:

```text
Congratulations! You won a FREE prize!!!
```

Salida:

```text
congratulations you won a free prize
```

---

## Vectorización

Se utiliza:

```text
TF-IDF Vectorizer
```

para transformar texto en características numéricas.

---

## Clasificador

Modelo implementado:

```text
Multinomial Naive Bayes
```

---

# Resultados Iniciales

Entrenamiento realizado sobre SMS Spam Collection.

Resultados obtenidos:

| Métrica  | Valor  |
| -------- | ------ |
| Accuracy | 96.05% |

---

# Estructura del Proyecto

```text
DetectSpam/
│
├── app/
│   ├── main.py
│   ├── schemas.py
│   │
│   ├── services/
│   │   └── predictor.py
│   │
│   ├── ml/
│   │   ├── preprocessing.py
│   │   ├── train_model.py
│   │   └── models/
│   │
│   ├── templates/
│   │   └── index.html
│   │
│   └── static/
│       ├── css/
│       └── js/
│
├── data/
│   ├── smsspam/
│   └── spambase/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Instalación

## Clonar repositorio

```bash
git clone <repository_url>
```

## Crear entorno virtual

```bash
python -m venv .venv
```

## Activar entorno virtual

Windows:

```bash
.venv\Scripts\activate
```

Linux/Mac:

```bash
source .venv/bin/activate
```

## Instalar dependencias

```bash
pip install -r requirements.txt
```

---

# Entrenamiento del Modelo

Ejecutar:

```bash
python app/ml/train_model.py
```

El modelo será generado automáticamente en:

```text
app/ml/models/spam_model.joblib
```

---

# Ejecución de la Aplicación

Iniciar FastAPI:

```bash
uvicorn app.main:app --reload
```

Abrir navegador:

```text
http://127.0.0.1:8000
```

Swagger:

```text
http://127.0.0.1:8000/docs
```

---

# Funcionalidades Implementadas

## Backend

* API REST con FastAPI
* Endpoint de predicción
* Endpoint health check
* Documentación Swagger

## Machine Learning

* Entrenamiento automatizado
* Persistencia del modelo
* Clasificación SPAM / NO SPAM

## Frontend

* Interfaz web responsiva
* Visualización de confianza
* Explicación básica
* Botón limpiar

---

# Relación con la Asignatura Hackeando la IA

La detección de SPAM constituye uno de los primeros problemas de seguridad abordados mediante técnicas de Inteligencia Artificial.

Este proyecto permite comprender conceptos asociados a:

* Clasificación supervisada
* Ingeniería de características
* Procesamiento de lenguaje natural
* Seguridad ofensiva y defensiva
* Manipulación de entradas adversariales
* Robustez de modelos de IA

Asimismo, establece una base para futuras investigaciones relacionadas con:

* Prompt Injection
* Jailbreaking
* Adversarial Machine Learning
* Model Poisoning
* Detección de contenido malicioso

---

# Trabajo Futuro

* Precision
* Recall
* F1 Score
* Matriz de Confusión
* Dashboard de métricas
* Historial de análisis
* Explicaciones XAI
* Modelos Transformer
* BERT
* Detección de mensajes adversariales
* Integración con LLMs

---

# Licencia

Proyecto desarrollado exclusivamente con fines académicos y educativos.

Universidad Icesi
Maestría en Inteligencia Artificial
Asignatura: Hackeando la IA
2026

---

# Autores

**Alfredo Aponte**
Arquitecto SAP BTP | Especialista en IA y Transformación Digital

**Arlex Pino**
Maestría en Inteligencia Artificial - Universidad Icesi
