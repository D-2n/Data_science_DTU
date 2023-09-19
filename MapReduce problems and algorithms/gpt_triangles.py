# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 16:45:28 2023

@author: dimit
"""
import time
st = time.time()
from collections import defaultdict

# Function to read edges from a file and build a graph representation
def build_graph_from_file(filename):
    graph = defaultdict(set)
    with open(filename, 'r') as file:
        for line in file:
            u, v = map(int, line.strip().split())
            graph[u].add(v)
            graph[v].add(u)
    return graph

# Function to count the number of triangles in a graph
def count_triangles(graph):
    triangle_count = 0
    for node in graph:
        neighbors = graph[node]
        for neighbor1 in neighbors:
            for neighbor2 in neighbors:
                if neighbor1 != neighbor2 and neighbor1 in graph[neighbor2]:
                    triangle_count += 1
    # Each triangle is counted 6 times (once for each of its 3 nodes), so divide by 6
    return triangle_count // 6

if __name__ == "__main__":
    filename = "data/roadnet.txt"
    graph = build_graph_from_file(filename)
    num_triangles = count_triangles(graph)
    print(f"Number of triangles in the graph: {num_triangles}")
    

et = time.time()
print('Time taken: ', et - st)  