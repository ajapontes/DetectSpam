from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.schemas import PredictionRequest, PredictionResponse
from app.services.predictor import predictor

app = FastAPI(
    title="DetectSpam",
    description="Aplicación web para detectar mensajes SPAM usando Machine Learning",
    version="1.0.0",
)

app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "app_name": "DetectSpam"},
    )


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "message": "DetectSpam API is running",
    }


@app.post("/predict", response_model=PredictionResponse)
def predict_spam(request: PredictionRequest):
    result = predictor.predict(request.text)
    return result