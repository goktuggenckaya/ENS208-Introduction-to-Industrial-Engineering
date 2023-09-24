"""
ENS 208 - Introduction to IE

Constructs a TSP solution using the nearest neighbor algorithm and improves it
using the 2-opt algorithm.
"""

import pandas as pd
from TSPalgos import nearest_neighbor, two_opt

# Read the distance matrix from the excel file tsp_data
df = pd.read_excel('tsp_data.xls')
#print(df.shape)

# List of nodes
nodes = list(range(df.shape[0]))

# Build distance matrix
d = [[round(float(df[j][i]), 2) for j in nodes] for i in nodes]

origin = 0 # origin for the TSP tour

# Call the nearest neighbor function to construct a TSP tour via NNH
tour, tour_length = nearest_neighbor(nodes, origin, d)
print('TSP tour found with nearest neighbor search starting from', origin, 
          'is', tour, 'with total length', tour_length)

# Start with the tour found by NNH and improve it via 2-opt until no further 
# improvement is achieved
# Call the 2-opt function
tour, tour_length = two_opt(tour, tour_length, d)
# Print the best solution found as a result of the improvement phase
print('Improved TSP tour is', tour, 'with total length', tour_length)