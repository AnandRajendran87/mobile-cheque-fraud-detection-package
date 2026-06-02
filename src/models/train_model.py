import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib

DATA_PATH = "data/sample/sample_cheque_features.csv"
MODEL_PATH = "src/models/cheque_fraud_model.joblib"

def train():
    df = pd.read_csv(DATA_PATH)
    X = df[["image_quality_score","signature_match_score","layout_anomaly_score","tamper_score","duplicate_score"]]
    y = df["fraud_label"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
    model = RandomForestClassifier(n_estimators=100, random_state=42, class_weight="balanced")
    model.fit(X_train, y_train)
    print(classification_report(y_test, model.predict(X_test), zero_division=0))
    joblib.dump(model, MODEL_PATH)

if __name__ == "__main__":
    train()
