from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import joblib

# Initialize app and template engine
app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

# Load model and vectorizer
try:
    model = joblib.load("models/fake_news_model.pkl")
    vectorizer = joblib.load("models/vectorizer.pkl")
except Exception as e:
    print(f"❌ Error loading model or vectorizer: {e}")
    raise HTTPException(status_code=500, detail="Model loading failed")

# Define input format for API
class NewsItem(BaseModel):
    text: str

# HTML frontend route
@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Prediction API
@app.post("/predict")
def predict(item: NewsItem):
    try:
        vector = vectorizer.transform([item.text])
        prediction = model.predict(vector)[0]
        return {"prediction": "REAL" if prediction == 1 else "FAKE"}
    except Exception as e:
        print(f"❌ Prediction error: {e}")
        raise HTTPException(status_code=500, detail="Prediction failed")
