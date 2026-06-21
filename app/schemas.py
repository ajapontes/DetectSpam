from pydantic import BaseModel, Field


class PredictionRequest(BaseModel):
    text: str = Field(
        ...,
        min_length=1,
        description="Mensaje que se desea analizar",
    )


class PredictionResponse(BaseModel):
    prediction: str
    confidence: float
    message: str
    explanation: str
