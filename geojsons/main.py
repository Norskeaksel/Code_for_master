import geopandas as gpd
import matplotlib.pyplot as plt

NO = gpd.read_file('NO1.geojson')
NO1 = [gpd.read_file('NO'+str(i)+'.geojson') for i in range(1,6)]
ax = NO.plot(color='blue')
plt.show()