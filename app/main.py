from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib

app = FastAPI()

try:
    model = joblib.load("models/fake_news_model.pkl")
    vectorizer = joblib.load("models/vectorizer.pkl")
except Exception as e:
    print(f"❌ Error loading model or vectorizer: {e}")
    raise HTTPException(status_code=500, detail="Model loading failed")

class NewsItem(BaseModel):
    text: str

@app.post("/predict")
def predict(item: NewsItem):
    try:
        vector = vectorizer.transform([item.text])
        prediction = model.predict(vector)[0]
        return {"prediction": "REAL" if prediction == 1 else "FAKE"}
    except Exception as e:
        print(f"❌ Prediction error: {e}")
        raise HTTPException(status_code=500, detail="Prediction failed")