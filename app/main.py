from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()

model = joblib.load("models/fake_news_model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")

class NewsItem(BaseModel):
    text: str

@app.post("/predict")
def predict(item: NewsItem):
    vector = vectorizer.transform([item.text])
    prediction = model.predict(vector)[0]
    return {"prediction": "REAL" if prediction == 1 else "FAKE"}
