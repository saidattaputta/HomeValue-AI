import pandas as pd

from fastapi import APIRouter, HTTPException

from api.schemas import (
    HousePredictionRequest,
    BatchPredictionRequest,
    PredictionResponse,
    BatchPredictionResponse
)

from src.pipelines.pipeline import PredictionPipeline

router = APIRouter()

pipeline = PredictionPipeline()

@router.get('/')
def home():

    return {
        "message": "Welcome to Home Value AI API"
    }

@router.get('/health')
def health():

    return {
        "status": "healthy"
    }

@router.post(
    '/predict',
    response_model=PredictionResponse
)
def pridict(request: HousePredictionRequest):

    try:

        df = pd.DataFrame([request.features])

        prediction = pipeline.predict(df)

        return PredictionResponse(
            predicted_price=float(prediction[0])
        )
    
    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
    
@router.post(
    '/batch_predict',
    response_model=BatchPredictionResponse
)
def batch_predict(request: BatchPredictionRequest):

    try:

        df = pd.DataFrame(request.houses)

        predictions = pipeline.predict(df)

        return BatchPredictionResponse(
            predictions=predictions.tolist()
        )
    
    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )