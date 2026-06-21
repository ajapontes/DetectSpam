from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.schemas import PredictionRequest, PredictionResponse
from app.services.predictor import predictor


# Create the FastAPI application instance
app = FastAPI(
    title="DetectSpam",
    description="Web application for detecting SPAM messages using Machine Learning",
    version="1.0.0",
)


# Mount the static directory to serve CSS and JavaScript files
app.mount("/static", StaticFiles(directory="app/static"), name="static")


# Configure the templates directory for rendering HTML pages
templates = Jinja2Templates(directory="app/templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    """
    Render the main web interface.

    Args:
        request (Request): Incoming HTTP request object required by Jinja2.

    Returns:
        TemplateResponse: Rendered HTML page for the DetectSpam application.
    """
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "app_name": "DetectSpam"},
    )


@app.get("/health")
def health_check():
    """
    Health check endpoint.

    This endpoint is used to verify that the API is running correctly.

    Returns:
        dict: API status information.
    """
    return {
        "status": "ok",
        "message": "DetectSpam API is running",
    }


@app.post("/predict", response_model=PredictionResponse)
def predict_spam(request: PredictionRequest):
    """
    Predict whether a submitted text message is spam or ham.

    Args:
        request (PredictionRequest): Request body containing the text message.

    Returns:
        PredictionResponse: Prediction result, confidence score, original message,
        and explanation.
    """
    result = predictor.predict(request.text)
    return result