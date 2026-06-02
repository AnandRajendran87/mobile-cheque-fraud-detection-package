import joblib
import pandas as pd

FEATURE_COLUMNS = ["image_quality_score","signature_match_score","layout_anomaly_score","tamper_score","duplicate_score"]

def score_cheque(features: dict, model_path: str = "src/models/cheque_fraud_model.joblib") -> dict:
    model = joblib.load(model_path)
    X = pd.DataFrame([features])[FEATURE_COLUMNS]
    fraud_probability = float(model.predict_proba(X)[0][1])
    if fraud_probability >= 0.75:
        decision = "REVIEW_HIGH_RISK"
    elif fraud_probability >= 0.45:
        decision = "STEP_UP_REVIEW"
    else:
        decision = "APPROVE"
    return {
        "fraud_probability": round(fraud_probability, 4),
        "decision": decision,
        "reason_codes": generate_reason_codes(features)
    }

def generate_reason_codes(features: dict):
    reasons = []
    if features.get("tamper_score", 0) > 0.6:
        reasons.append("High image tampering risk")
    if features.get("signature_match_score", 1) < 0.5:
        reasons.append("Low signature similarity")
    if features.get("duplicate_score", 0) > 0.5:
        reasons.append("Potential duplicate or resubmission")
    if features.get("layout_anomaly_score", 0) > 0.5:
        reasons.append("Abnormal cheque layout")
    return reasons
