import pandas as pd

df = pd.read_csv("datasets/processed_events.csv")

print("=" * 50)
print("DATASET SHAPE")
print(df.shape)

print("\nCOLUMNS")
print(df.columns.tolist())

print("\nEVENT TYPE DISTRIBUTION")
if "event_type" in df.columns:
    print(df["event_type"].value_counts())

print("\nPRIORITY DISTRIBUTION")
if "priority" in df.columns:
    print(df["priority"].value_counts())

print("\nNUMERIC COLUMNS")
print(df.select_dtypes(include=["int64", "float64"]).columns.tolist())

print("\nMISSING VALUES")
print(df.isnull().sum())