# HomeValue AI

An end-to-end Machine Learning application for predicting residential house prices using the Ames Housing Dataset.

The project demonstrates the complete lifecycle of a production-ready ML system, including data preprocessing, feature engineering, model training, explainability, REST API development, and an interactive web dashboard.

## Features

- Single House Price Prediction
- Batch House Price Prediction
- SHAP Explainability
- FastAPI REST API
- Streamlit Dashboard
- Model Insights
- Automated Feature Engineering
- Production-ready Preprocessing Pipeline

## Tech Stack

### Machine Learning
- Python
- Scikit-learn
- SHAP
- Pandas
- NumPy

### Backend
- FastAPI
- Uvicorn

### Frontend
- Streamlit

### Visualization
- Matplotlib
- SHAP

### Version Control
- Git
- GitHub

## Project Structure

```text
HomeValue-AI/
│
├── api/
├── app/
│   ├── pages/
│   └── components/
│
├── src/
│   ├── data/
│   ├── features/
│   ├── models/
│   ├── pipelines/
│   ├── preprocessing/
│   ├── utils/
│   └── visualization/
│
├── artifacts/
├── models/
├── data/
│
├── train.py
├── requirements.txt
└── README.md
```

## Machine Learning Pipeline

```text
Raw Dataset
      │
      ▼
Data Cleaning
      │
      ▼
Feature Engineering
      │
      ▼
Preprocessing Pipeline
      │
      ▼
Model Training
      │
      ▼
SHAP Explainability
      │
      ▼
FastAPI REST API
      │
      ▼
Streamlit Dashboard
```

## Machine Learning Model

- Algorithm: Ridge Regression
- Dataset: Ames Housing
- Problem Type: Regression
- Explainability: SHAP

## Application Pages

- Home
- House Price Prediction
- Batch Prediction
- Model Insights
- About

## Installation

Clone the repository

```bash
git clone https://github.com/your-username/HomeValue-AI.git
cd HomeValue-AI
```

Install dependencies

```bash
pip install -r requirements.txt
```

## Train the Model

```bash
python train.py
```

## Run FastAPI

```bash
uvicorn api.main:app --reload
```

API Documentation

```
http://127.0.0.1:8000/docs
```

## Run Streamlit

```bash
streamlit run app/app.py
```

## Screenshots

- Home Page
- Prediction Page
- Batch Prediction
- Model Insights
- API Documentation

## Future Improvements

- Docker Deployment
- Cloud Deployment
- CI/CD Pipeline
- Model Monitoring
- Experiment Tracking
- User Authentication
- Model Versioning

## Author

**Sai Datta Putta**

Integrated M.Sc Mathematics

National Institute of Technology Warangal

Machine Learning | Data Science | AI

