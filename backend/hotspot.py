import pandas as pd

df = pd.read_csv("datasets/processed_events.csv")

location_column = None

for col in [
    "junction",
    "corridor",
    "zone",
    "gba_identifier"
]:
    if col in df.columns:
        location_column = col
        break

if location_column is None:
    print("No location column found")
    exit()

hotspots = (
    df.groupby(location_column)
      .size()
      .sort_values(ascending=False)
      .head(10)
)

print("\nTop Traffic Hotspots\n")
print(hotspots)