import networkx as nx
import matplotlib.pyplot as plt
from geopy.geocoders import Nominatim
import random
import numpy as np


import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from geopy.geocoders import Nominatim






class Plot:

    def __init__(self):
        pass

    def plot_routes(self,name='route', routes=None):
        G = nx.Graph(name=name)
        line = []
        line.append(routes)
        edges = []
        for r in line:
            route_edges = [(r[n], r[n + 1]) for n in range(len(r) - 1)]
            G.add_nodes_from(r)
            G.add_edges_from(route_edges)
            edges.append(route_edges)

        print("Graph has %d nodes with %d edges" % (G.number_of_nodes(),
                                                    G.number_of_edges()))

        pos = nx.spring_layout(G)
        nx.draw_networkx_nodes(G, pos=pos)
        nx.draw_networkx_labels(G, pos=pos)
        colors = ['b', 'b', 'y']
        linewidths = [3, 10, 5]
        for ctr, edgelist in enumerate(edges):
            nx.draw_networkx_edges(G, pos=pos, edgelist=edgelist, edge_color=colors[ctr], width=linewidths[ctr])
        plt.axis('off')
        plt.show()
        plt.close()
        plt.savefig('this.png')



    def plot_city_in_map(self,routes=None):
        geolocator = Nominatim()
        fig = plt.figure(num=None, figsize=(150, 150))
        m = Basemap(projection='merc', llcrnrlat=-80, urcrnrlat=80, llcrnrlon=-180, urcrnrlon=180, resolution='c')
        m.drawcoastlines()
        m.fillcontinents(color='tan', lake_color='lightblue')
        # draw parallels and meridians.
        m.drawmapboundary(fill_color='lightblue')

        nylat = 40.78;
        nylon = -73.98
        # lonlat, lonlon are lat/lon of London.
        lonlat = 51.53;
        lonlon = 0.08
        # draw great circle route between NY and London
        # m.drawgreatcircle(nylon, nylat, lonlon, lonlat, linewidth=2, color='b')
        last_long=0
        last_lat=0
        count=0
        for city in routes:
            loc = geolocator.geocode(city)
            # x, y = map(loc.longitude, loc.latitude)
            if (count !=0) :
                print('lala: %s' % count)
                print(loc)
                m.drawgreatcircle(last_long, last_lat, loc.longitude, loc.latitude, linewidth=2, color='b')
            x, y = m(loc.longitude, loc.latitude)
            m.plot(x,y,'b', markersize=50)
            plt.text(x, y, city,fontsize=8 ,fontweight='bold', ha='left',va='top',color='k')
            last_long = loc.longitude
            last_lat = loc.latitude
            count+=1
        plt.show()

lal= Plot()
lal.plot_city_in_map(routes=['Sydney','Tokio','Londres', 'Mexico DF'])
