import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

import joblib

# =========================
# Load dataset
# =========================
df = pd.read_csv("data/placement_cleaned.csv")

# Drop salary if exists
if "salary" in df.columns:
    df = df.drop("salary", axis=1)

# =========================
# Encode categorical columns
# =========================
df_encoded = df.copy()

for col in df_encoded.columns:
    if df_encoded[col].dtype == "object":
        le = LabelEncoder()
        df_encoded[col] = le.fit_transform(df_encoded[col])

# =========================
# FINAL SELECTED FEATURES (IMPORTANT FIX)
# =========================
features = [
    "ssc_p",
    "hsc_p",
    "degree_p",
    "etest_p",
    "mba_p",
    "workex"
]

X = df_encoded[features]
y = df_encoded["status"]

# =========================
# Train-test split
# =========================
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# =========================
# Logistic Regression
# =========================
print("========== Logistic Regression ==========")

lr = LogisticRegression(max_iter=1000)
lr.fit(X_train, y_train)

pred1 = lr.predict(X_test)

print("Accuracy:", accuracy_score(y_test, pred1))
print(classification_report(y_test, pred1))
print(confusion_matrix(y_test, pred1))

print("\n")

# =========================
# Random Forest
# =========================
print("========== Random Forest ==========")

rf = RandomForestClassifier(random_state=42)
rf.fit(X_train, y_train)

pred2 = rf.predict(X_test)

print("Accuracy:", accuracy_score(y_test, pred2))
print(classification_report(y_test, pred2))
print(confusion_matrix(y_test, pred2))

# =========================
# Feature Importance
# =========================
importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": rf.feature_importances_
})

importance = importance.sort_values(by="Importance", ascending=False)

print("\nTop Important Features:")
print(importance)

# =========================
# Save model
# =========================
joblib.dump(rf, "placement_model.pkl")
print("\nModel saved as placement_model.pkl")