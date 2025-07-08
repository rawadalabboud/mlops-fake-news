# 🧠 Fake News Classifier API

A machine learning API that classifies news articles as **REAL** or **FAKE** using a logistic regression model and TF-IDF vectorizer.

Built with:
- FastAPI (for serving predictions)
- Docker (for containerization)
- scikit-learn (for ML)
- Render (for deployment)

---

## 🚀 Live Demo

👉 [Access the API on Render](https://mlops-fake-news.onrender.com/docs)

Use the `/predict` endpoint with a POST request like:

```json
{
  "text": "NASA just launched a new mission to study exoplanets."
}


🧰 Project Structure
mlops-fake-news/
├── app/
│   └── main.py          # FastAPI app
├── data/
│   ├── Fake.csv
│   └── True.csv         # Training data
├── models/
│   ├── fake_news_model.pkl
│   └── vectorizer.pkl   # Trained model + preprocessor
├── train.py             # Model training script
├── requirements.txt     # Python dependencies
├── Dockerfile           # Container build instructions
├── .dockerignore        # Clean up Docker context
├── render.yaml          # Render deployment config
└── README.md            # You're here!

🏗️ How to Run Locally

1. Clone the repo
git clone https://github.com/rawadalabboud/mlops-fake-news.git
cd mlops-fake-news
2. Set up virtual environment
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
3. Train the model
python train.py
4. Run the API
uvicorn app.main:app --reload
Visit: http://localhost:8000/docs

🐳 Run with Docker

docker build -t fake-news-api .
docker run -p 8000:8000 fake-news-api
📦 Deploy to Render

Just connect your repo to Render, and it will automatically deploy using render.yaml.

📌 Todo / Future Ideas

✅ Add tests for /predict
🧠 Try better models (e.g., BERT)
💻 Add a simple frontend with HTML or Gradio
🧪 Add CI/CD with GitHub Actions
👤 Author

Rawad Al Abboud — rawadalabboud