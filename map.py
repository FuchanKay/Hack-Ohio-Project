import pypsa
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point, LineString
from shapely.affinity import translate
import contextily as ctx


network = pypsa.Network("example_csv")

    buses = network.buses.copy()
    buses["geometry"] = [Point(xy) for xy in zip(buses["x"], buses["y"])]
    gdf_buses = gpd.GeoDataFrame(buses, geometry="geometry", crs="EPSG:4326")

lines = network.lines.copy()
lines["geometry"] = [
    LineString([
        (network.buses.at[bus0, "x"], network.buses.at[bus0, "y"]),
        (network.buses.at[bus1, "x"], network.buses.at[bus1, "y"])
    ])
    for bus0, bus1 in zip(lines["bus0"], lines["bus1"])
]
gdf_lines = gpd.GeoDataFrame(lines, geometry="geometry", crs="EPSG:4326")

    # project to Web Mercator (required by contextily)
    gdf_buses = gdf_buses.to_crs(epsg=3857)
    gdf_lines = gdf_lines.to_crs(epsg=3857)

    # compute bounds and add padding in meters (increase pad to "zoom out")
    minx, miny, maxx, maxy = gdf_buses.total_bounds
    pad_meters = 10000  # <-- increase to "zoom out" more (10 km here)
    minx -= pad_meters; miny -= pad_meters; maxx += pad_meters; maxy += pad_meters

fig, ax = plt.subplots(figsize=(11, 9))
gdf_lines.plot(ax=ax, color="dimgray", linewidth=1.2, zorder=2)
gdf_buses.plot(ax=ax, color="crimson", markersize=35, zorder=3)

    # Add basemap (Esri WorldTopoMap)
    ctx.add_basemap(ax, source=ctx.providers.Esri.WorldTopoMap, crs='EPSG:3857')

    # set the extent to our padded bounds
    ax.set_xlim(minx, maxx)
    ax.set_ylim(miny, maxy)

    ax.set_axis_off()
    plt.tight_layout()
    plt.show()