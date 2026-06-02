from src.inference.score_cheque import generate_reason_codes

def test_reason_codes_high_tamper():
    reasons = generate_reason_codes({
        "tamper_score": 0.8,
        "signature_match_score": 0.9,
        "duplicate_score": 0.1,
        "layout_anomaly_score": 0.1
    })
    assert "High image tampering risk" in reasons
