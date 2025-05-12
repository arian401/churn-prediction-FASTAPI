# Customer Churn Prediction API – Retail Analytics with Machine Learning

This project demonstrates how to build, deploy, and automate a **churn prediction system** for a retail or e-commerce platform using **machine learning** and **FastAPI**.

## Overview

To implement automated **retail analytics with machine learning**, the process begins by training predictive models—such as churn prediction, price sensitivity modeling, or customer segmentation—using business-specific data like customer activity and purchase history. This is typically done in a Python script or Jupyter notebook where the model is trained, evaluated, and saved as a `.pkl` file along with any preprocessing tools like scalers.

In this example, customer churn prediction is based on data extracted from a PostgreSQL e-commerce database using SQLAlchemy. The model is trained and exposed via a FastAPI endpoint for real-time prediction integration with the business backend.

---

## ⚙️ Features

- ✅ Connect to a live PostgreSQL database
- ✅ Load and preprocess customer records
- ✅ Train a classification model (Random Forest)
- ✅ Export model and scaler as `.pkl` files
- ✅ Serve predictions through a FastAPI POST endpoint
- ✅ Supports JSON input for integration into dashboards or web backends

---

## 🗂️ Project Structure

```
.
├── main.py                  # FastAPI app
├── train_and_export.py      # Training + export script
├── models/
│   ├── churn_model.pkl      # Trained model
│   └── scaler.pkl           # Scaler used during preprocessing
├── requirements.txt         # Required Python packages
└── README.md                # Project documentation
```

---

## Run Locally

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Train the model and generate `.pkl` files
```bash
python train_and_export.py
```

> This script connects to a PostgreSQL database, loads customer data using SQLAlchemy, trains a churn prediction model, and exports it.

### 3. Launch the API
```bash
uvicorn main:app --reload
```

### 4. Open in browser (Swagger UI)
```
http://127.0.0.1:8000/docs
```

---

## Example JSON Input

```json
{
  "tenure_months": 12,
  "total_spent": 350.50,
  "avg_purchase_frequency": 3.2,
  "is_active": 1
}
```

---

## 🌐 Deployment Options

You can host the app and model on:

- **Render.com** (via GitHub auto-deploy)
- **Hugging Face Spaces** (Git-based auto-rebuild)
- **Streamlit** (as UI layer for business teams)

---

## 🔁 Automation Pipeline

To apply the models continuously:

- Pull live customer data from DB or dashboard via API
- Call the model API for predictions
- Trigger business actions based on predictions

For ongoing effectiveness, establish a **weekly retraining pipeline** using:

- `cron` jobs
- **Apache Airflow**
- **GitHub Actions**

The workflow will:
1. Pull fresh data
2. Retrain and generate new `.pkl` files
3. Push to GitHub or Hugging Face → auto-redeploy

This end-to-end automation ensures that ML insights stay relevant and actionable without manual intervention.

---

## Contact

For questions, feedback, or collaboration, feel free to open an issue or reach out.
