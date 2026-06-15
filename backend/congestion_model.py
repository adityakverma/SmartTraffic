import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from catboost import CatBoostClassifier
from sklearn.metrics import accuracy_score
import joblib

print("Loading dataset...")

df = pd.read_csv("datasets/processed_events.csv")

# Features
features = [
    "zone",
    "junction",
    "hour",
    "day_of_week",
    "month",
    "year"
]

X = df[features]
y = df["congestion_risk"]

categorical_features = [
    "zone",
    "junction"
]

numerical_features = [
    "hour",
    "day_of_week",
    "month",
    "year"
]

preprocessor = ColumnTransformer(
    transformers=[
        (
            "cat",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_features
        )
    ],
    remainder="passthrough"
)

model = CatBoostClassifier(
    iterations=1000,
    learning_rate=0.05,
    depth=8,
    verbose=100
)

pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("model", model)
])

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("Training model...")

pipeline.fit(X_train, y_train)

predictions = pipeline.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("\nModel Accuracy:", accuracy)

joblib.dump(
    pipeline,
    "models/congestion_model.pkl"
)

print("Model saved.")