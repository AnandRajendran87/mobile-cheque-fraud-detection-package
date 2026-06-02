# Computer Vision for Mobile Cheque Fraud Detection

## Overview

This repository contains a reusable AI-driven document forensics framework for detecting fraud in mobile cheque deposits. The solution uses computer vision, deep learning, image preprocessing, signature analysis, handwriting anomaly detection, and explainable AI to identify altered, forged, counterfeit, duplicate, or manipulated cheque images.

The framework is designed for digital banking, mobile remote deposit capture, financial crime prevention, and enterprise risk intelligence environments.

## Business Problem

Mobile cheque deposits remain widely used across the United States, especially by small businesses, older consumers, rural communities, and underbanked populations. Fraudsters exploit remote deposit channels by submitting altered cheque images, forged signatures, counterfeit instruments, duplicate deposits, and manipulated cheque images.

Traditional controls often rely on metadata checks, thresholds, manual image review, and post-deposit reconciliation. These methods can miss subtle visual manipulation and can become costly at scale.

## Solution

The proposed platform treats cheque images as forensic documents. Each cheque image is processed through a computer vision pipeline that detects tampering artifacts, abnormal layout patterns, signature inconsistencies, duplicate submissions, and suspicious field-level changes.

The platform produces a fraud risk score and routes high-risk deposits to an analyst review queue with explainable AI indicators.

## Key Capabilities

- Mobile cheque image preprocessing
- Cheque layout validation
- Amount and payee field tampering detection
- Signature consistency analysis
- Handwriting anomaly detection
- Duplicate and resubmission detection
- Counterfeit cheque pattern detection
- Deep learning-based image classification
- Explainable AI heatmaps
- Analyst review workflow
- Model monitoring and governance controls

## Architecture

The high-level architecture includes:

1. Mobile cheque image upload
2. Image quality validation
3. Preprocessing and normalization
4. Cheque region detection
5. Feature extraction
6. Computer vision fraud detection engine
7. Signature and handwriting analysis
8. Duplicate/resubmission detection
9. Fraud risk scoring API
10. Analyst investigation dashboard
11. Model monitoring and governance

See `architecture/mobile_cheque_fraud_architecture.md`.

## Repository Structure

```text
mobile-cheque-fraud-detection-package/
├── architecture/
├── data/sample/
├── dashboards/
├── docs/
├── notebooks/
├── screenshots/
├── src/
│   ├── api/
│   ├── governance/
│   ├── inference/
│   ├── models/
│   └── preprocessing/
├── tests/
├── whitepapers/
└── README.md
```

## Example Use Cases

### Altered Amount Detection
Detects overwritten or manipulated numeric and written amount fields.

### Payee Tampering Detection
Identifies suspicious modifications in payee name regions.

### Signature Forgery Detection
Compares signature patterns against historical customer signatures.

### Duplicate Deposit Detection
Detects reuse of previously deposited cheque images.

### Counterfeit Cheque Detection
Identifies abnormal layout, missing security features, inconsistent fonts, or suspicious print patterns.

### Image Manipulation Detection
Detects blur, splicing artifacts, compression inconsistencies, and edited cheque regions.

## Technology Stack

- Python
- OpenCV
- PyTorch
- TensorFlow/Keras
- FastAPI
- scikit-learn
- NumPy
- Pandas
- SHAP / Grad-CAM
- Docker
- MLflow

## Sample Metrics

Expected validation targets for a controlled pilot environment:

- 90–95% detection accuracy under controlled validation
- 30–50% reduction in manual review volume
- Earlier identification of altered and counterfeit cheques
- Reduced post-deposit fraud losses
- Improved analyst prioritization

## Responsible AI and Governance

This project includes documentation for explainability, audit logging, model monitoring, drift detection, controlled model lifecycle management, and human-in-the-loop fraud review.

## Disclaimer

This repository is for educational, research, and enterprise architecture demonstration purposes. It does not contain confidential banking data, proprietary fraud rules, customer information, or production system details.
