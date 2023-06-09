import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import community

net = open('Hi-tech.net')
G = nx.read_pajek('Hi-tech.net')

# create a list of nodes and arcs stored in nodes and arcs respectively
nodes = list(G.nodes)
arcs = list(G.edges)
arcs = [(i[0],i[1]) for i in arcs ]

plt.figure(figsize=(100, 180))

# create edge colors
edge_colors = ['red', 'blue', 'green', 'orange']

# create an undirected graph using nx
f = nx.Graph()

# Add nodes
f.add_nodes_from(nodes)

# Add edges
f.add_edges_from(arcs)

# spring layout for better visual analysis
pos = nx.spring_layout(f)

# Scale the positions of the nodes for better visual analysis
scale_factor = 10.0
scaled_pos = {node: pos[node] * scale_factor for node in G.nodes()}
nx.draw_networkx_nodes(f, pos=scaled_pos, node_color='lightblue', node_size=50)
nx.draw_networkx_edges(f, pos=scaled_pos, edge_color=edge_colors, arrows=True)
nx.draw_networkx_labels(f, pos=scaled_pos, font_size=10, font_family='sans-serif')

# Show the plot
#plt.show()

# Compute the partition using Louvain method
partition = community.best_partition(f)

# Compute the modularity
modularity = community.modularity(partition, f)

print("Modularity:", modularity)

# modularity value of 0.303526 obtained





