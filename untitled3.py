# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1j021bLWdKSQ33KDh0NWZy5t91tDe9Oqf
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from imblearn.over_sampling import SMOTE

# Step 1: Load the dataset

data = pd.read_csv("creditcard.csv")

# Step 2: Data Preprocessing
# Check for missing values
print("Missing values:\n", data.isnull().sum())

data.columns

# Drop rows with missing values in the target column 'Class'
data = data.dropna(subset=["Class"])

# Separate features and labels
X = data.drop(columns=["Class"])
y = data["Class"]

# Handle class imbalance using SMOTE
smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X, y)

# Step 3: Split the data
X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled, test_size=0.2, random_state=42)

# Step 4: Train the model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Step 5: Make predictions
y_pred = model.predict(X_test)

# Step 6: Evaluate the model
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))
print("Accuracy Score:\n", accuracy_score(y_test, y_pred))

# Step 7: Save the model (optional)
import joblib
joblib.dump(model, "fraud_detection_model.pkl")

