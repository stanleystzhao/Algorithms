#ifndef DIJKSTRA_H
#define DIJKSTRA_H

#include "adjlist.h"

// Function to find the minimum distance vertex 
// from the set of vertices not yet included in the shortest path tree
int minDistance(int dist[], bool sptSet[], int V);

// Recursive function to print the path from source to j
// using the parent array
void printPath(Graph* graph, int parent[], int j);

// Function to print the solution
void printSolution(Graph* graph, int dist[], int parent[], int V, int src, int dest);

// Function to find the shortest path using Dijkstra's algorithm
void dijkstra(Graph* graph, int src, int dest);

#endif
