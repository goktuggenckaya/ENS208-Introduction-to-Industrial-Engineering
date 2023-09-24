"""
ENS 208 Fall 2020

HIGHLIGHTS:
1. Constructs a feasible VRP solution by cluster-first-route-second algorithm.
2. Constructs a feasible VRP solution by route-first-cluster-second algorithm.
3. Improves the VRP solution by applying 2-opt within each vehicle's route.
4. Plots the final (improved) VRP solution.
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from TSPalgos import two_opt
from VRPalgos import CFRS, RFCS

# Read distance matrix from the excel file real_distances_40customers
df = pd.read_excel('Question4Nodes.xlsx')

# List of nodes
nodes = list(range(df.shape[0]))

# Build distance matrix
d = [[round(float(df[j][i]), 2) for j in nodes] for i in nodes]

# Read the x and y coordinates of the nodes from the excel file coordinates
dfCoor = pd.read_excel('coordinates.xls') # dataframe

# Node coordinates
node_coordinates = {i: (dfCoor["x-coordinate"][i], dfCoor["y-coordinate"][i]) for i in nodes}
coordinates = np.array([i for i in node_coordinates.values()])

#Draw node locations
plt.scatter(coordinates[:,0], coordinates[:,1])
# plt.show()
plt.axis('off')
plt.savefig("nodes.png")


# # =============================================================================
# Construct a VRP solution using cluster-first-route-second heuristic
# =============================================================================
k = 5 
vrp_solution, total_length = CFRS(k, coordinates, d, plt)
print("The VRP solution obtained by CFRS procedure:\n", vrp_solution, "with a"
       " total length of", total_length)

# =============================================================================
# Construct a VRP solution using route-first-cluster-second heuristic when k
# vehicles are available
# =============================================================================
#k = 5 # number of vehicles available
#vrp_solution, total_length = RFCS(k, nodes, d)
#print("The VRP solution obtained by RFCS procedure:\n", vrp_solution, "with a"
#     " total length of", total_length, "when", k, "vehicles are available")
#
# =============================================================================
# Improvement with 2-opt (intra-route swaps)
# =============================================================================
improved_vrp_solution = []
improved_total_length = 0
for tour in vrp_solution:
    tour_length = sum(d[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    new_tour, new_tour_length = two_opt(tour, tour_length, d)
    improved_vrp_solution.append(new_tour)
    improved_total_length += new_tour_length
print("The improved VRP solution:\n", improved_vrp_solution, "with a total"
      " length of", improved_total_length)

# =============================================================================
# Plot the final VRP solution
# =============================================================================
import networkx as nx
G = nx.DiGraph()
for i in nodes:
    G.add_node(i, pos = node_coordinates[i])
for tour in vrp_solution:
    for i in range(len(tour)-1):
        G.add_edge(tour[i],tour[i+1])

pos = nx.get_node_attributes(G, 'pos')
plt.figure(figsize=(30, 16))

customers = [i for i in G.nodes if i != 0]
nx.draw_networkx_nodes(G, pos, nodelist = [0], node_color = 'magenta', alpha = 0.6, node_size = 500)
nx.draw_networkx_nodes(G, pos, nodelist = customers, node_color = 'greenyellow', alpha = 0.8, node_size = 500)
nx.draw_networkx_labels(G, pos)

nx.draw_networkx_edges(G, pos, G.edges, arrows = True, width = 4,  alpha = 0.3, edge_color = 'blue')
plt.axis('off')
#plt.show()
plt.savefig("vrp_solution.png")