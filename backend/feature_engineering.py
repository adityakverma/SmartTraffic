import pandas as pd

df = pd.read_csv(
    "datasets/clean_astram_events.csv"
)

df["start_datetime"] = pd.to_datetime(
    df["start_datetime"],
    errors="coerce"
)

# Time features

df["hour"] = (
    df["start_datetime"]
    .dt.hour
)

df["day_of_week"] = (
    df["start_datetime"]
    .dt.dayofweek
)

df["month"] = (
    df["start_datetime"]
    .dt.month
)

df["year"] = (
    df["start_datetime"]
    .dt.year
)

# Target label

def congestion_label(priority):

    priority = str(priority).lower()

    if "critical" in priority:
        return "High"

    if "high" in priority:
        return "High"

    if "medium" in priority:
        return "Medium"

    return "Low"

df["congestion_risk"] = (
    df["priority"]
    .apply(congestion_label)
)

df.to_csv(
    "datasets/processed_events.csv",
    index=False
)

print("Processed dataset saved.")