# Mobile Cheque Fraud Detection Architecture

```mermaid
flowchart TD
    A[Mobile Banking App] --> B[Cheque Image Upload]
    B --> C[Image Quality Validation]
    C --> D[Preprocessing & Normalization]
    D --> E[Cheque Region Detection]
    E --> F[Field Extraction: Amount, Payee, Date, MICR, Signature]
    F --> G[Computer Vision Fraud Detection Engine]
    G --> H[Signature & Handwriting Analysis]
    G --> I[Image Tampering Detection]
    G --> J[Counterfeit Layout Detection]
    G --> K[Duplicate / Resubmission Detection]
    H --> L[Fraud Risk Scoring API]
    I --> L
    J --> L
    K --> L
    L --> M{Decision Engine}
    M -->|Low Risk| N[Approve Deposit]
    M -->|Medium Risk| O[Step-Up Review]
    M -->|High Risk| P[Analyst Investigation Queue]
    P --> Q[Case Management]
    L --> R[Explainable AI Heatmaps]
    R --> P
    L --> S[Monitoring, Drift Detection & Governance]
```

## Component Description

The architecture begins when a customer submits a cheque image through a mobile banking application. The image quality validation layer checks focus, lighting, orientation, glare, cropping, and resolution. The preprocessing layer normalizes the cheque image using denoising, edge detection, perspective correction, grayscale conversion, contrast enhancement, and segmentation.

The cheque region detection layer identifies key areas such as amount, payee, date, MICR line, memo, signature, and endorsement. Computer vision models then evaluate visual inconsistencies, tampering artifacts, signature anomalies, handwriting inconsistencies, counterfeit layout indicators, and duplicate submission patterns.

The fraud risk scoring API generates a risk score and supporting reason codes. Low-risk deposits proceed automatically, medium-risk deposits may require additional validation, and high-risk deposits are routed to analysts for review.
