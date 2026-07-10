from typing import Any
from pydantic import BaseModel

class HousePredictionRequest(BaseModel):

    features: dict[str,Any]

class BatchPredictionRequest(BaseModel):

    houses: list[dict[str,Any]]

class PredictionResponse(BaseModel):

    predicted_price: float

class BatchPredictionResponse(BaseModel):

    predictions: list[float]

