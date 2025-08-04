from fastapi import FastAPI
import joblib
import psycopg2
import os
from datetime import datetime

app = FastAPI()
classifier = joblib.load('../checkpoint/tfidf_classifier.pkl')
vectorizer = joblib.load('../checkpoint/tfidf_vectorizer.pkl')
username = os.getenv('postgreUsername')
password = os.getenv('postgrePassword')

@app.get("/health")
def health():
    return {"status": "ok"}


def get_db_connection():
    return psycopg2.connect(
        host="localhost",
        database="news",
        user=username,
        password=password
    )

@app.get("/classify")
def classify(text: str):
    #Transform text using trained vectorizer
    text_vector = vectorizer.transform([text])

    prediction = classifier.predict(text_vector)[0]
    confidence = classifier.predict_proba(text_vector).max()

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO predictions (input_text, predicted_label, confidence_score) VALUES (%s, %s, %s)",
            (text, prediction, float(confidence))
        )

        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        print(e)
    
    return {
        "predicted_category": prediction,
        "confidence": round(float(confidence), 4),
        "timestamp": datetime.now().isoformat()
    }
