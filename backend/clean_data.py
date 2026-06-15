import pandas as pd

print("Loading dataset...")

df = pd.read_csv("datasets/astram_events.csv")

print("Rows:", len(df))
print("Columns:", len(df.columns))

# Convert datetime columns

datetime_cols = [
    "start_datetime",
    "end_datetime",
    "created_date",
    "closed_datetime",
    "resolved_datetime"
]

for col in datetime_cols:
    if col in df.columns:
        df[col] = pd.to_datetime(
            df[col],
            errors="coerce"
        )

# Fill missing categorical values

categorical_cols = [
    "event_type",
    "event_cause",
    "corridor",
    "zone",
    "junction",
    "veh_type"
]

for col in categorical_cols:
    if col in df.columns:
        df[col] = df[col].fillna("Unknown")

df.to_csv(
    "datasets/clean_astram_events.csv",
    index=False
)

print("Clean dataset saved.")