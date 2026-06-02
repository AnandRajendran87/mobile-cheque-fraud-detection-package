import cv2
import numpy as np

def preprocess_cheque_image(image_path: str):
    """Load and normalize a cheque image for fraud analysis."""
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Image not found: {image_path}")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    denoised = cv2.fastNlMeansDenoising(gray)
    enhanced = cv2.equalizeHist(denoised)
    resized = cv2.resize(enhanced, (1024, 512))
    return resized

def image_quality_score(image: np.ndarray) -> float:
    """Simple focus quality score using Laplacian variance."""
    variance = cv2.Laplacian(image, cv2.CV_64F).var()
    return min(float(variance / 1000.0), 1.0)
