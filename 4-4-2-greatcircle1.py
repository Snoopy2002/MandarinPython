#city distance on world map

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import math

global RADIUS
RADIUS = 6378.1

global DC
DC=180/math.pi #for conversion of radians to degrees

global milestokm
kmtomiles=0.62137 #for converting miles to km

global DR #for converting degrees to radians
DR=math.pi/180


def haversin(Lat, Long): #haversine distance function
    
    Hlat=math.pow(math.sin((Lat[1]-Lat[0])/2),2)
    Hlong=math.pow(math.sin((Long[1]-Long[0])/2),2)
    return(Hlat, Hlong)
    
def radianconvert(A): #converts to radian measure
    for i in range(len(A)):
        A[i]=A[i]*DR
    return(A)
    
def DrawMap(Lat, Long, city, m): #draws the map
    
    
    code=0
    s2='miles between cities'
    k=str(int(m))
    print(k)
    s2.join(k)
    
        
    for x in range(0,len(Lat)): #converts radians back to degrees for plotting
        Lat[x]=DC*Lat[x]
        Long[x]=DC*Long[x]
    try:
      m = Basemap(projection = 'eck4', llcrnrlat=-45, urcrnrlat=45,
        llcrnrlon=-170, urcrnrlon=170, lon_0=0, lat_0=0, resolution='l')

      m.drawcoastlines()
      m.fillcontinents (color='lightgray', lake_color='blue')
      m.drawparallels(np.arange(-90.,91.,30.))
      m.drawmeridians(np.arange(-180.,181.,60.))
      m.drawmapboundary(fill_color='aqua')
      m.drawmapscale(lat=-20,lon=-140,lat0=0, lon0=0, length=1000)
      m.drawrivers(linewidth=0.2)
      x,y=m(Long,Lat)
      #m.scatter(Long, Lat, marker = 'x', color='r', zorder=5)
      m.drawgreatcircle(Long[0],Lat[0],Long[1],Lat[1],linewidth=2,color='r')
      
      for c, xpt, ypt in zip(city, x, y):
          plt.text(xpt, ypt-1000, c, size='x-large', color='black')
          
      plt.title('World Map', size='large')
      plt.annotate(s2, xy=(0,1),xycoords='axes fraction')
      plt.show()
      code=1
      return(code)
    except:
      return(code)
    
    
if __name__ == "__main__":   
  Lat=[]
  Long=[]
  city=[]
  
  city.append(input("Enter the first city name: "))
  Lat.append(float(input("Enter the first latitude: ")))
  Long.append(float(input("Enter the first longitude: ")))
  city.append(input("Enter the second city name: "))
  Lat.append(float(input("Enter the second latitude: ")))
  Long.append(float(input("Enter the second longitude: ")))


  Lat=radianconvert(Lat)
  Long=radianconvert(Long)


  H1,H2=haversin(Lat, Long)
  d=2*RADIUS*math.asin(math.sqrt((H1+math.cos(Lat[0])*math.cos(Lat[1])*H2)))
  miles=d*kmtomiles
  print("The distance between the two points on the Earth is {:12.4f} " .format(d), " kilometers. ")
  print("this is {:12.4f}".format(miles), "miles." )
  isok=DrawMap(Lat, Long, city, miles)
  if isok == 0:
      print("Error in plotting.")

    
    