import pandas as pd
import folium
from folium.plugins import HeatMap

df = pd.read_csv("datasets/processed_events.csv")

lat_col = None
lon_col = None

for col in df.columns:
    if "latitude" in col.lower():
        lat_col = col

    if "longitude" in col.lower():
        lon_col = col

print(lat_col)
print(lon_col)

heat_data = df[[lat_col, lon_col]].dropna().values.tolist()

m = folium.Map(
    location=[
        df[lat_col].mean(),
        df[lon_col].mean()
    ],
    zoom_start=11
)

HeatMap(heat_data).add_to(m)

m.save("heatmap.html")

print("Heatmap saved.")