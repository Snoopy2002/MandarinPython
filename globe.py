import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

austin = (-97.75, 30.25)
hawaii = (-157.8, 21.3)
washington = (-77.01, 38.90)
chicago = (-87.68, 41.83)
losangeles = (-118.25, 34.05)

m = Basemap(projection = 'robin', llcrnrlat=-45, urcrnrlat=45,
        llcrnrlon=-170, urcrnrlon=170, lon_0=0, lat_0=0, resolution='i')

m.drawcoastlines()
m.fillcontinents (color='lightgray', lake_color='aqua')
m.drawparallels(np.arange(-90.,91.,30.))
m.drawmeridians(np.arange(-180.,181.,60.))
m.drawmapboundary(fill_color='blue')
m.drawmapscale(lat=-20,lon=-140,lat0=0, lon0=0, length=500)
m.drawrivers(linewidth=0.2)

m.drawcountries()

#x, y = m(*zip(*[hawaii, austin, washington, chicago, losangeles]))
#m.plot(x,y, marker ='o', markersize=6, markerfacecolor='red', linewidth=0)
m.drawgreatcircle(austin[0],austin[1],chicago[0],chicago[1])
plt.title('World Map')
plt.show()