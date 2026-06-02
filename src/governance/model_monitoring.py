from dataclasses import dataclass

@dataclass
class MonitoringMetrics:
    accuracy: float
    false_positive_rate: float
    manual_review_rate: float
    drift_score: float

def evaluate_monitoring_status(metrics: MonitoringMetrics) -> str:
    if metrics.drift_score > 0.25:
        return "MODEL_DRIFT_REVIEW_REQUIRED"
    if metrics.false_positive_rate > 0.15:
        return "FALSE_POSITIVE_REVIEW_REQUIRED"
    return "STABLE"
