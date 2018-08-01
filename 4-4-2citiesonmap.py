#city distance on world map
#takes two cities, latitude and longitude and plots them on a world map
#with a great circle route

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
    s2=' miles between cities'
    k=str(int(m))
    s3 = k + s2
    
        
    for x in range(0,len(Lat)): #converts radians back to degrees for plotting
        Lat[x]=DC*Lat[x]
        Long[x]=DC*Long[x]
    #print(Long[0], Long[1])
    #print(Lat[0], Lat[1])
    try:
        
      print("Enter the number of the type of map projection you wish to see. \n")
      project_method=input("1-Orthographic 2-Equidistant Cylindrical 3-Mercator 4-Robinson 5-Gall 6-Mollweide 0-Blue Marble only: ")
      res=input("\nEnter the desired resolution of the map you want: l=low, i=intermediate, h=high, f=full : ")
      
      if project_method == '0': #blue marble only
          m = Basemap(projection='ortho', resolution=res, lat_0=Lat[0], lon_0=Long[0])
          m.bluemarble(scale=0.75);
      
      if project_method == '1': #orthographic
          p='ortho'
          m = Basemap(projection=p,lon_0=int((Long[0]+Long[1])/2),lat_0=int(Lat[0]),resolution=res)
         
          
      elif project_method == '2': #van der Grinten
          p='vandg'
          m = Basemap(projection='vandg',lon_0=(Long[0]+Long[1])/2,resolution=res)
          
          
      elif project_method == '3': #mercator
          p='merc'
          m = Basemap(llcrnrlon=-180.,llcrnrlat=-60.,urcrnrlon=180,urcrnrlat=70,
            rsphere=(6378137.00,6356752.3142),
            resolution=res,projection=p,
            lat_0=Lat[0],lon_0=Long[0])
          
      elif project_method == '4': #robinson
          p='robin'
          m = Basemap(projection = p, lon_0=int(Long[0]), resolution=res)
          
          
      elif project_method == '5': #gall
          p='gall'
          m = Basemap(projection = p, llcrnrlat=-90, urcrnrlat=90,
          llcrnrlon=-180, urcrnrlon=180, resolution=res)
          
          
      elif project_method == '6': #mollweide projection
          p='moll'
          m = Basemap(projection = p, lon_0=int(Long[0]), resolution=res)
          
     
      else:
          print("incorrect value entered, default to robinson projection ") #default to robinson projection
          p='robin'
          m = Basemap(projection = p, lon_0=int(Long[0]), resolution=res)
      
      if project_method == '0':
        
         plt.title('World Map Orthographic Projection Blue Marble', size='x-large')
         plt.show()
         code=1
         return(code)
          
      if project_method == '1': #orthographic
         m.drawcoastlines()
         m.fillcontinents(color='coral',lake_color='aqua')
         # draw parallels and meridians.
         m.drawparallels(np.arange(-90.,120.,30.))
         m.drawmeridians(np.arange(0.,420.,60.))
         m.drawmapboundary(fill_color='aqua')
         m.drawrivers(linewidth=0.2)
         x,y=m(Long,Lat)
         for c, xpt, ypt in zip(city, x, y):
           plt.text(xpt, ypt-1000, c, size='x-large', color='black', weight='bold')
         m.drawgreatcircle(Long[0],Lat[0],Long[1],Lat[1],linewidth=2,color='r') #draws the great circle route on map
         plt.title('World Map Orthographic Projection', size='large')
         plt.annotate(s3, xy=(2,200), xytext=(2,2))
         plt.show()
         code=1
         return(code)
         
      if project_method == '2': #van der Grinten
          m.drawcoastlines()
          m.fillcontinents(color='coral',lake_color='aqua')
         # draw parallels and meridians.
          m.drawparallels(np.arange(-80.,81.,20.))
          m.drawmeridians(np.arange(0.,360.,60.))
          m.drawmapboundary(fill_color='aqua')
          m.drawrivers(linewidth=0.2)
          x,y=m(Long,Lat)
          for c, xpt, ypt in zip(city, x, y):
            plt.text(xpt, ypt-1000, c, size='x-large', color='black', weight='bold')
          m.drawgreatcircle(Long[0],Lat[0],Long[1],Lat[1],linewidth=2,color='r') #draws the great circle route on map
          plt.title('World Map Van der Grinten Projection', size='large')
          plt.annotate(s3, xy=(2,200), xytext=(2,2))
          plt.show()
          code=1
          return(code)
         
      if project_method == '3': #Mercator
         m.drawcoastlines()
         m.fillcontinents(color='coral',lake_color='aqua')
         # draw parallels and meridians.
         m.drawparallels(np.arange(10,90,20),labels=[1,1,0,1])
         m.drawmeridians(np.arange(-180,180,30),labels=[1,1,0,1])
         m.drawmapboundary(fill_color='aqua')
         m.drawmapscale(lat=-40,lon=-140,lat0=0, lon0=0, length=1000)
         m.drawrivers(linewidth=0.2)
         x,y=m(Long,Lat)
         for c, xpt, ypt in zip(city, x, y):
           plt.text(xpt, ypt-1000, c, size='x-large', color='black', weight='bold')
         m.drawgreatcircle(Long[0],Lat[0],Long[1],Lat[1],linewidth=2,color='r') #draws the great circle route on map

         plt.title('World Map Mercator Projection', size='large')
         plt.annotate(s3, xy=(2,200), xytext=(2,2))
         plt.show()
         code=1
         return(code)
      
      if project_method > '3': #robinson/gall/mollweide
        m.fillcontinents (color='lightgray', lake_color='blue')
        m.drawparallels(np.arange(-90.,120.,30.))
        m.drawmeridians(np.arange(0.,360.,60.))
        m.drawmapboundary(fill_color='aqua')
        m.drawmapscale(lat=-20,lon=-140,lat0=0, lon0=0, length=1000)
        m.drawrivers(linewidth=0.2)
        x,y=m(Long,Lat)
        #m.scatter(Long, Lat, marker = 'x', color='r', zorder=5)
        m.drawgreatcircle(Long[0],Lat[0],Long[1],Lat[1],linewidth=2,color='r') #draws the great circle route on map
      
        for c, xpt, ypt in zip(city, x, y):
           plt.text(xpt, ypt-1000, c, size='x-large', color='black', weight='bold')
        
        
        if project_method == 4:
            plt.title('World Map Robinson Projection', size='large')
        if project_method == 5:
            plt.title('World Map Gall Projection', size='large')
        if project_method == 6:
           plt.title('World Map Mollweide Projection', size='large')
        plt.annotate(s3, xy=(2,200), xytext=(2,2))
        plt.show()
        code=1
        return(code)
    
            
    except:
          return(code) #error in plot
    
    
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

    
    