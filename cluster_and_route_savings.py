"""
ENS 208 - Introduction to IE

Constructs a feasible VRP solution by constructing TSP tours for given node 
clusters using savings algorithm.
"""

import pandas as pd
from TSPalgos import savings

# Read the distance matrix from the excel file real_distances_40customers
df = pd.read_excel('real_distances_40customers.xls')
#print(df.shape)

# List of nodes
nodes = list(range(df.shape[0]))

# Build distance matrix
d = [[round(float(df[j][i]), 2) for j in nodes] for i in nodes]

# Origin for every vehicle's route
origin = 0

# Define the node clusters (these clusters are the ones given in the lecture slides)
clusters = [[2, 3, 10, 11, 15, 20, 28, 29, 31, 35, 37, 38, 39, 40],
            [5, 6, 7, 8, 12, 13, 16, 18, 21, 22, 25, 30, 33, 34],
            [1, 4, 9, 14, 17, 19, 23, 24, 26, 27, 32, 36]]

# Initialize the VRP solution to be an ampty list and the total distance traveled
# by the vehicles to be equal to zero
vrp_solution = []
vrp_total_distance = 0

# Call the savings function for every cluster c
for c in clusters:
    tour, tour_length = savings(c, origin, d)
    vrp_solution.append(tour)
    vrp_total_distance += tour_length

print("The VRP solution is:")
for tour in vrp_solution:
    print(tour)
print("with total distance", vrp_total_distance)