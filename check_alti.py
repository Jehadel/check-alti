import os
import rioxarray as rxr
import geopandas as gpd
import pyproj
from shapely.geometry import Point
import matplotlib.pyplot as plt

dalleShp_path = r'BDALTIV2_2-0_25M_ASC_LAMB93-IGN69_D005_2021-08-04/BDALTIV2/3_SUPPLEMENTS_LIVRAISON_2021-10-00008/BDALTIV2_MNT_25M_ASC_LAMB93_IGN69_D005'

dalleShp_file = 'dalles.shp'

gdf = gpd.read_file(os.path.join(dalleShp_path, dalleShp_file))

crs_origin = 'WGS84'
crs_target = pyproj.CRS(gdf.crs) # à priori Lambert93

transformer = pyproj.Transformer.from_crs(crs_origin, crs_target, always_xy=True)

#coordonnées points recherché
lat = 44.881112
lon = 6.634004

x, y = transformer.transform(lon, lat)

point = Point(x, y)

dalle_name = gdf[gdf.geometry.contains(point)].iloc[0].NOM_DALLE + '.asc'

dalle_path = r'BDALTIV2_2-0_25M_ASC_LAMB93-IGN69_D005_2021-08-04/BDALTIV2/1_DONNEES_LIVRAISON_2021-10-00008/BDALTIV2_MNT_25M_ASC_LAMB93_IGN69_D005'


DS = rxr.open_rasterio(os.path.join(dalle_path, dalle_name))

#DS.plot(cmap = 'terrain', vmin=100, vmax=300)
DS.plot()
plt.show()

print(float(DS.sel(x=x, y=y, method='nearest')))
