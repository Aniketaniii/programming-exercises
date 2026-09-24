"""
simple_fraud_detection.py
--------------------------
A SIMPLE, single-file version of the fraud detection project.
Good for understanding the core idea and for explaining in a viva.

Steps in this one file:
    1. Create a small transaction dataset
    2. Split into train/test
    3. Train ONE model (Random Forest)
    4. Test it and print accuracy
    5. Try a new transaction and see if it's flagged as fraud

Run:
    pip install pandas scikit-learn
    python simple_fraud_detection.py
"""

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# ------------------------------------------------------
# STEP 1: Create a simple dataset
# (amount, hour of day, is_new_device, is_foreign_country) -> is_fraud
# ------------------------------------------------------
data = {
    "amount":            [500, 1200, 800, 95000, 300, 45000, 2000, 60000, 700, 50000,
                           600, 1500, 900, 70000, 400, 55000, 1100, 40000, 250, 65000],
    "hour_of_day":       [14, 10, 16, 2, 13, 3, 11, 1, 15, 4,
                           12, 9, 17, 2, 14, 3, 10, 1, 16, 4],
    "is_new_device":     [0, 0, 0, 1, 0, 1, 0, 1, 0, 1,
                           0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
    "is_foreign_country":[0, 0, 0, 1, 0, 1, 0, 1, 0, 1,
                           0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
    "is_fraud":          [0, 0, 0, 1, 0, 1, 0, 1, 0, 1,
                           0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
}
df = pd.DataFrame(data)
print("Sample data:\n", df.head(), "\n")

# ------------------------------------------------------
# STEP 2: Split into features (X) and label (y), then train/test
# ------------------------------------------------------
X = df[["amount", "hour_of_day", "is_new_device", "is_foreign_country"]]
y = df["is_fraud"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# ------------------------------------------------------
# STEP 3: Train a model
# ------------------------------------------------------
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# ------------------------------------------------------
# STEP 4: Test the model
# ------------------------------------------------------
predictions = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, predictions))
print(classification_report(y_test, predictions, target_names=["Legit", "Fraud"]))

# ------------------------------------------------------
# STEP 5: Check a brand-new transaction
# ------------------------------------------------------
new_transaction = pd.DataFrame([{
    "amount": 80000,
    "hour_of_day": 3,
    "is_new_device": 1,
    "is_foreign_country": 1,
}])

risk = model.predict_proba(new_transaction)[0][1] * 100
print(f"\nNew transaction fraud risk: {risk:.0f}%")
print("Result:", "FRAUD - Block transaction" if risk > 50 else "Looks legitimate")