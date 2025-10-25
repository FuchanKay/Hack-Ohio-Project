import pypsa
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point, LineString
from shapely.affinity import translate
import contextily as ctx
import numpy as np

network = pypsa.Network("example_csv")

buses = network.buses.copy()
buses["geometry"] = [Point(xy) for xy in zip(buses["x"], buses["y"])]
gdf_buses = gpd.GeoDataFrame(buses, geometry="geometry", crs="EPSG:4326")

lines = network.lines.copy()
geoms = []

offset_distance = 0.002  # degrees, adjust for clarity
for i, (bus0, bus1) in enumerate(zip(lines["bus0"], lines["bus1"])):
    x0, y0 = network.buses.at[bus0, "x"], network.buses.at[bus0, "y"]
    x1, y1 = network.buses.at[bus1, "x"], network.buses.at[bus1, "y"]
    line_geom = LineString([(x0, y0), (x1, y1)])
    
    # Check for duplicates
    count = sum(((lines["bus0"] == bus0) & (lines["bus1"] == bus1)) |
                ((lines["bus0"] == bus1) & (lines["bus1"] == bus0)))
    if count > 1:
        # Offset each parallel line by a small perpendicular distance
        angle = np.arctan2(y1 - y0, x1 - x0)
        dx = np.sin(angle) * offset_distance * (i % count - count / 2)
        dy = -np.cos(angle) * offset_distance * (i % count - count / 2)
        line_geom = translate(line_geom, xoff=dx, yoff=dy)
    
    geoms.append(line_geom)

lines["geometry"] = geoms
gdf_lines = gpd.GeoDataFrame(lines, geometry="geometry", crs="EPSG:4326")

# project to Web Mercator (required by contextily)
gdf_buses = gdf_buses.to_crs(epsg=3857)
gdf_lines = gdf_lines.to_crs(epsg=3857)

# compute bounds and add padding in meters (increase pad to "zoom out")
minx, miny, maxx, maxy = gdf_buses.total_bounds
pad_meters = 10000  # <-- increase to "zoom out" more (10 km here)
minx -= pad_meters; miny -= pad_meters; maxx += pad_meters; maxy += pad_meters

fig, ax = plt.subplots(figsize=(11, 9))
gdf_lines.plot(ax=ax, color="green", linewidth=1.3, alpha=0.8, zorder=1)
gdf_buses.plot(ax=ax, color="red", markersize=30, zorder=2)



# Add bus labels
for x, y, label in zip(gdf_buses.geometry.x, gdf_buses.geometry.y, gdf_buses.index):
    ax.text(x, y, label, fontsize=7, ha='right', color='black', zorder=3)

# Add line labels
for _, row in gdf_lines.iterrows():
    mid = row.geometry.interpolate(0.5, normalized=True)
    ax.text(mid.x, mid.y, row.name, fontsize=6, color='darkgreen', zorder=3)
    

# Add basemap (Esri WorldTopoMap)
ctx.add_basemap(ax, source=ctx.providers.Esri.WorldTopoMap, crs='EPSG:3857')

# set the extent to our padded bounds
ax.set_xlim(minx, maxx)
ax.set_ylim(miny, maxy)

ax.set_axis_off()
plt.tight_layout()
plt.show()