# main.py
#from map_plotter import MapPlotter
from DFS_FC import DFS_FC
from dfs_MRV import dfsMRV
from DFS_DC import DFS_DC
from dfs import DFS
from DFS_FC_MRV import FC_MRV
from DFS_FC_DegreeC import FC_DegreeC

import networkx as nx

def main():

    # Create a new map
   # map_plotter = MapPlotter(100, -45, 165, -5, 'l', 4326)
  #  map_plotter.draw_map()

    # Create the graph
    graph = nx.Graph()
    graph.add_edges_from([('AL', 'GA'), ('AL', 'TN'), ('AL', 'MS'), ('AL', 'FL'),
                        ('AK','AK'),
                        ('AZ', 'CA'), ('AZ', 'NV'), ('AZ', 'UT'), ('AZ', 'CO'), ('AZ', 'NM'),
                        ('AR', 'MO'), ('AR', 'TN'), ('AR', 'MS'), ('AR', 'LA'), ('AR', 'TX'), ('AR', 'OK'),
                        ('CA', 'OR'), ('CA', 'NV'), ('CA', 'AZ'),
                        ('CO', 'WY'), ('CO', 'NE'), ('CO', 'KS'), ('CO', 'OK'), ('CO', 'NM'), ('CO', 'UT'),
                        ('CT', 'RI'), ('CT', 'MA'), ('CT', 'NY'),
                        ('DE', 'MD'), ('DE', 'PA'), ('DE', 'NJ'),
                        ('FL', 'AL'), ('FL', 'GA'),
                        ('GA', 'TN'), ('GA', 'NC'), ('GA', 'SC'), ('GA', 'AL'), ('GA', 'FL'),
                        ('HI','HI'),
                        ('ID', 'MT'), ('ID', 'WY'), ('ID', 'UT'), ('ID', 'NV'), ('ID', 'OR'), ('ID', 'WA'),
                        ('IL', 'WI'), ('IL', 'IA'), ('IL', 'MO'), ('IL', 'KY'), ('IL', 'IN'),
                        ('IN', 'MI'), ('IN', 'IL'), ('IN', 'OH'), ('IN', 'KY'),
                        ('IA', 'MN'), ('IA', 'WI'), ('IA', 'IL'), ('IA', 'MO'), ('IA', 'NE'), ('IA', 'SD'),
                        ('KS', 'NE'), ('KS', 'MO'), ('KS', 'OK'), ('KS', 'CO'),
                        ('KY', 'IL'), ('KY', 'IN'), ('KY', 'OH'), ('KY', 'WV'), ('KY', 'VA'), ('KY', 'TN'), ('KY', 'MO'),
                        ('LA', 'AR'), ('LA', 'MS'), ('LA', 'TX'),
                        ('ME', 'NH'),
                        ('MD', 'PA'), ('MD', 'DE'), ('MD', 'VA'), ('MD', 'WV'),
                        ('MA', 'NH'), ('MA', 'VT'), ('MA', 'NY'), ('MA', 'RI'), ('MA', 'CT'),
                        ('MI', 'WI'), ('MI', 'MN'), ('MI', 'IN'), ('MI', 'OH'),
                        ('MN', 'ND'), ('MN', 'SD'), ('MN', 'IA'), ('MN', 'WI'), ('MN', 'MI'),
                        ('MS', 'TN'), ('MS', 'AL'), ('MS', 'AR'), ('MS', 'LA'),
                        ('MO', 'IA'), ('MO', 'IL'), ('MO', 'KY'), ('MO', 'TN'), ('MO', 'AR'), ('MO', 'OK'), ('MO', 'KS'), ('MO', 'NE'),
                        ('MT', 'ND'), ('MT', 'SD'), ('MT', 'WY'), ('MT', 'ID'),
                        ('NE', 'SD'), ('NE', 'IA'), ('NE', 'MO'), ('NE', 'KS'), ('NE', 'CO'), ('NE', 'WY'),
                        ('NV', 'OR'), ('NV', 'ID'), ('NV', 'UT'), ('NV', 'CA'),
                        ('NH', 'ME'), ('NH', 'VT'), ('NH', 'MA'),
                        ('NJ', 'NY'), ('NJ', 'PA'), ('NJ', 'DE'),
                        ('NM', 'CO'), ('NM', 'OK'), ('NM', 'TX'), ('NM', 'AZ'), ('NM', 'UT'),
                        ('NY', 'VT'), ('NY', 'MA'), ('NY', 'CT'), ('NY', 'NJ'), ('NY', 'PA'),
                        ('NC', 'VA'), ('NC', 'TN'), ('NC', 'GA'), ('NC', 'SC'),
                        ('ND', 'MN'), ('ND', 'SD'), ('ND', 'MT'),
                        ('OH', 'MI'), ('OH', 'IN'), ('OH', 'KY'), ('OH', 'WV'), ('OH', 'PA'),
                        ('OK', 'KS'), ('OK', 'MO'), ('OK', 'AR'), ('OK', 'TX'), ('OK', 'NM'), ('OK', 'CO'),
                        ('OR', 'WA'), ('OR', 'ID'), ('OR', 'NV'), ('OR', 'CA'),
                        ('PA', 'NY'), ('PA', 'NJ'), ('PA', 'DE'), ('PA', 'MD'), ('PA', 'WV'), ('PA', 'OH'),
                        ('RI', 'MA'), ('RI', 'CT'),
                        ('SC', 'NC'), ('SC', 'GA'),
                        ('SD', 'ND'), ('SD', 'MN'), ('SD', 'IA'), ('SD', 'NE'), ('SD', 'WY'), ('SD', 'MT'),
                        ('TN', 'KY'), ('TN', 'VA'), ('TN', 'NC'), ('TN', 'GA'), ('TN', 'AL'), ('TN', 'MS'), ('TN', 'AR'), ('TN', 'MO'),
                        ('TX', 'NM'), ('TX', 'OK'), ('TX', 'AR'), ('TX', 'LA'),
                        ('UT', 'ID'), ('UT', 'WY'), ('UT', 'CO'), ('UT', 'AZ'), ('UT', 'NV'),
                        ('VT', 'NY'), ('VT', 'NH'), ('VT', 'MA'),
                        ('VA', 'MD'), ('VA', 'WV'), ('VA', 'KY'), ('VA', 'TN'), ('VA', 'NC'),
                        ('WA', 'OR'), ('WA', 'ID'),
                        ('WV', 'OH'), ('WV', 'PA'), ('WV', 'MD'), ('WV', 'VA'), ('WV', 'KY'),
                        ('WI', 'MI'), ('WI', 'MN'), ('WI', 'IA'), ('WI', 'IL'),
                        ('WY', 'MT'), ('WY', 'SD'), ('WY', 'NE'), ('WY', 'CO'), ('WY', 'UT')])


    print("***************** DFS  **************************")
    dfs = DFS(graph)
    colors = dfs.run()
    print("Chromatic number:", max(colors.values()))

    # Create a mapping of color numbers to color names
    color_mapping = {
        1: 'red',
        2: 'blue',
        3: 'green',
        4: 'yellow',
        5: 'pink'
        #6: 'orange',
        #7: 'black',
        #8: 'grey',
        #9: 'purple',
        #10: 'white'
    }

    # Print the colors assigned to each node
    #for node, color in colors.items():
    #    print(f"{node}: {color}")

    for node, color_number in colors.items():
        color_name = color_mapping.get(color_number, f"unknown_color_{color_number}")
        print(f"{node}: {color_name}")

    print("***************** DFS_MRV  **************************")

    dfs_MRV = dfsMRV(graph)
    colors = dfs_MRV.run()

    # Create a mapping of color numbers to color names
    color_mapping = {
        1: 'red',
        2: 'blue',
        3: 'green',
        4: 'yellow',
        5: 'pink',
        6: 'orange',
        7: 'black',
        8: 'grey',
        9: 'purple',
        10: 'white'
    }

    # Print the colors assigned to each node
    # for node, color in colors.items():
    #    print(f"{node}: {color}")

    print("Chromatic number:", max(colors.values()))

    for node, color_number in colors.items():
        color_name = color_mapping.get(color_number, f"unknown_color_{color_number}")
        print(f"{node}: {color_name}")

    ##DFSwithDegreeConstraint

    print("***************** DFS_DC  **************************")

    dfs_DegreeConstraint = DFS_DC(graph)
    colors = dfs_DegreeConstraint.run()

    # Create a mapping of color numbers to color names
    color_mapping = {
        1: 'red',
        2: 'blue',
        3: 'green',
        4: 'yellow',
        5: 'pink',
        6: 'orange',
        7: 'black',
        8: 'grey',
        9: 'purple',
        10: 'white'
    }

    print("Chromatic number:", max(colors.values()))

    for node, color_number in colors.items():
        color_name = color_mapping.get(color_number, f"unknown_color_{color_number}")
        print(f"{node}: {color_name}")

    # Run Depth First Search with Forward Checking

    print("***************** DFS_FC  **************************")
    dfs_fc = DFS_FC(graph)
    colors = dfs_fc.run()
    print("Chromatic number:", max(colors.values()))

    # Create a mapping of color numbers to color names
    color_mapping = {
        1: 'red',
        2: 'blue',
        3: 'green',
        4: 'yellow',
        5: 'pink'
        #6: 'orange',
        #7: 'black',
        #8: 'grey',
        #9: 'purple',
        #10: 'white'
    }

    # Print the colors assigned to each node
    #for node, color in colors.items():
    #    print(f"{node}: {color}")

    for node, color_number in colors.items():
        color_name = color_mapping.get(color_number, f"unknown_color_{color_number}")
        print(f"{node}: {color_name}")

    print("***************** DFS_FC_MRV **************************")
    DFS_FC_MRV = FC_MRV(graph)
    colors = DFS_FC_MRV.run()
    print("Chromatic number:", max(colors.values()))

    # Create a mapping of color numbers to color names
    color_mapping = {
        1: 'red',
        2: 'blue',
        3: 'green',
        4: 'yellow',
        5: 'pink'
        # 6: 'orange',
        # 7: 'black',
        # 8: 'grey',
        # 9: 'purple',
        # 10: 'white'
    }

    # Print the colors assigned to each node
    # for node, color in colors.items():
    #    print(f"{node}: {color}")

    for node, color_number in colors.items():
        color_name = color_mapping.get(color_number, f"unknown_color_{color_number}")
        print(f"{node}: {color_name}")

    print("***************** DFS_FC_Degree Constraint **************************")
    DFS_FC_DegreeC = FC_DegreeC(graph)
    colors = DFS_FC_DegreeC.run()
    print("Chromatic number:", max(colors.values()))

    # Create a mapping of color numbers to color names
    color_mapping = {
        1: 'red',
        2: 'blue',
        3: 'green',
        4: 'yellow',
        5: 'pink'
        # 6: 'orange',
        # 7: 'black',
        # 8: 'grey',
        # 9: 'purple',
        # 10: 'white'
    }

    # Print the colors assigned to each node
    # for node, color in colors.items():
    #    print(f"{node}: {color}")

    for node, color_number in colors.items():
        color_name = color_mapping.get(color_number, f"unknown_color_{color_number}")
        print(f"{node}: {color_name}")


if __name__ == "__main__":
    main()
