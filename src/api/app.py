from fastapi import FastAPI
from pydantic import BaseModel
from src.inference.score_cheque import score_cheque

app = FastAPI(title="Mobile Cheque Fraud Detection API")

class ChequeFeatures(BaseModel):
    image_quality_score: float
    signature_match_score: float
    layout_anomaly_score: float
    tamper_score: float
    duplicate_score: float

@app.get("/")
def health_check():
    return {"status": "ok", "service": "mobile-cheque-fraud-detection"}

@app.post("/score")
def score(features: ChequeFeatures):
    return score_cheque(features.dict())
