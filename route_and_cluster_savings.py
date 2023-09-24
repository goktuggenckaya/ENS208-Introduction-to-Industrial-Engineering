# -*- coding: utf-8 -*-
"""
ENS 208 - Intro to IE

Route-and-cluster heuristic for the VRP which uses savings algorithm in the
routing phase
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

origin = 0 # origin for the vehicle routes

# Below is the tour given in Exercise 2
#tour = [0, 27, 36, 23, 26, 11, 39, 34, 33, 13, 16, 22, 30, 6, 25, 7, 12, 21, 
#        8, 18, 3, 31, 10, 20, 35, 40, 38, 2, 15, 37, 29, 28, 1, 24, 14, 4, 19, 
#        5, 17, 32, 9, 0]

# Construct a TSP tour over all nodes using savings algorithm
tour = savings(nodes, origin, d)[0]

vrp_solution = []
vrp_solution_length = 0
n_max = 15 # vehicle capacity
index = 1

for k in range(3):
    current_tour = [origin]
    current_nodes = 0
    while tour[index] != origin and current_nodes < n_max:
        current_tour.append(tour[index])
        current_nodes += 1
        index += 1
    current_tour.append(origin)
    vrp_solution.append(current_tour)

for r in vrp_solution:
    for i in range(len(r)-1):
        vrp_solution_length += d[r[i]][r[i+1]]
        
print("VRP solution obtained with route and cluster procedure is:",
      vrp_solution, "with total length",  vrp_solution_length)
        