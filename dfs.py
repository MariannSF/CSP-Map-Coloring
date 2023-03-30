from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.patches import Polygon

# create a new map
map = Basemap(llcrnrlon=100, llcrnrlat=-45, urcrnrlon=165, urcrnrlat=-5, resolution='l', epsg=4326)

# draw coastlines, countries, and states
map.drawcoastlines(linewidth=0.5)
map.drawcountries(linewidth=0.5)
map.drawstates(linewidth=0.5)

G = nx.Graph()

G.add_edges_from([('WA', 'NT'), ('WA', 'SA'), ('NT', 'SA'), ('NT', 'QLD'), ('SA', 'QLD'), ('SA', 'NSW'),
                  ('SA', 'VIC'), ('QLD', 'NSW'), ('NSW', 'VIC'),('TAS', 'TAS')])

colors = {}

# calculation of chromatic number using DFS
def dfs_chromatic(G, node, colors):
    used_colors = set(colors.get(neighbour) for neighbour in G[node] if neighbour in colors)
    for color in range(1, len(G) + 1):
        if color not in used_colors:
            colors[node] = color
            break
    for neighbour in G[node]:
        if neighbour not in colors:
            dfs_chromatic(G, neighbour, colors)


for node in G:
    dfs_chromatic(G, node, colors)




# define the latitude and longitude coordinates of each territory
latitudes = {'WA': [-35.1139, -23.8783, -26.0013, -34.0517, -35.1139],
             'NT': [-12.7419, -10.9392, -14.7875, -18.0014, -12.7419],
             'SA': [-25.9992, -29.1774, -32.3438, -31.0834, -29.1897, -26.6171, -25.9992],
             'QLD': [-12.3757, -16.0015, -28.1675, -29.9995, -29.0015, -9.1422],
             'NSW': [-28.1563, -31.9796, -36.1378, -34.9176, -34.0059, -34.0782, -31.5991, -28.1563],
             'VIC': [-36.7497, -36.5689, -37.5098, -39.1732, -38.5602, -36.8765, -36.7497],
             'TAS': [-43.6583, -40.2108, -40.8527, -42.0391, -42.9192, -43.6583]}

longitudes = {'WA': [113.6497, 114.1778, 118.0986, 129.0013, 113.6497],
              'NT': [129.0013, 135.0002, 137.9997, 129.0013, 129.0013],
              'SA': [129.0013, 129.0013, 140.9986, 140.9764, 135.0002, 132.2335, 129.0013],
              'QLD': [143.5150, 153.0000, 153.0026, 145.0002, 138.0002, 142.5249],
              'NSW': [141.0000, 141.0000, 149.9735, 150.6890, 149.0000, 144.0000, 141.0000, 141.0000],
              'VIC': [141.0000, 143.8789, 143.8345, 146.1450, 147.9998, 149.9815, 141.0000],
              'TAS': [144.4763, 144.1490, 146.4396, 146.8023, 148.3646, 146.8220]}


# define available colors
avalColors = plt.cm.get_cmap('Set1', max(colors.values()))

print("Chromatic number:", max(colors.values()))
# plot the territories with the assigned colors
# longitudes and latitudes may not be correct coloring is faulty
for region, color_index in colors.items():
    x, y = map(longitudes[region], latitudes[region])
    xy = list(zip(x, y))
    poly = Polygon(xy, facecolor=avalColors.colors[color_index - 1], edgecolor='k', linewidth=0.5, alpha=0.75, label=region)
    plt.gca().add_patch(poly)
    print(region, color_index)

# add a legend
plt.legend(loc='lower left')


plt.show()