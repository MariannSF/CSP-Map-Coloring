# map_plotter.py
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap


class MapPlotter:
    def __init__(self, llcrnrlon, llcrnrlat, urcrnrlon, urcrnrlat, resolution, epsg):
        self.map_obj = Basemap(llcrnrlon=llcrnrlon, llcrnrlat=llcrnrlat,
                               urcrnrlon=urcrnrlon, urcrnrlat=urcrnrlat,
                               resolution=resolution, epsg=epsg)

    def draw_map(self):
        self.map_obj.drawcoastlines(linewidth=0.5)
        self.map_obj.drawcountries(linewidth=0.5)
        self.map_obj.drawstates(linewidth=0.5)

        #plt.show()
