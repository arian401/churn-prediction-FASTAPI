#!/usr/bin/env python
# coding: utf-8

# # Automated Churn Prediction and Retail Optimization Using FastAPI and Airflow

#  
# ## 1.	Connect to your database, get the dataset
# Use SQLAlchemy or psycopg2 to connect to your database and extract relevant customer records.



from sqlalchemy import create_engine
import pandas as pd

# Replace with your credentials
username = "your_username"
password = "your_password"
host = "localhost"
port = "5432"
database = "your_database"

# Create engine
engine = create_engine(f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}")

# Sample SQL query to get customer data
query = """
SELECT
    customer_id,
    tenure_months,
    total_spent,
    avg_purchase_frequency,
    is_active,
    churned
FROM
    customer_data;
"""

# Load into pandas
df = pd.read_sql(query, engine)


# ## 2. Prepare the Dataset before ML
# Handle missing values, encode categorical variables, and scale numeric features.


# Define X and y
X = df[["tenure_months", "total_spent", "avg_purchase_frequency", "is_active"]]
y = df["churned"]

# Handle missing values or scaling if needed
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


# ## 3. Train the Model
# Use scikit-learn (or XGBoost, etc.) to fit a classification model.


from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Split data
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))


# ## 4. Save the Model as pkl files
# Export trained model and scaler (e.g., churn_model.pkl, scaler.pkl) using joblib.


import joblib

joblib.dump(model, "churn_model.pkl")
joblib.dump(scaler, "scaler.pkl")

