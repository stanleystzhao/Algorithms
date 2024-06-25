#include "dijkstra.h"
#include <limits.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int minDistance(int dist[], bool sptSet[], int V) {

    int min = INT_MAX;
    int min_index;

    for (int v = 0; v < V; v++)
        // if the vertex is not in the shortest path tree 
        // and the distance is less than the minimum
        if (sptSet[v] == false && dist[v] <= min)
        // update the minimum value and the index of the minimum value
            min = dist[v], min_index = v;

    return min_index;
}

void printPath(Graph* graph, int parent[], int j) {
    // if the graph is NULL, return
    if (graph == NULL) {return;}

    // Base Case : If j is the parent of the source vertex
    if (j == -1) {return;}

    // recursive call from the destination to the source
    printPath(graph, parent, parent[j]);

    // print from the source to the destination
    if (graph->array[j].name[0] != '\0') {
        printf("%s\n", graph->array[j].name);
    }

}

void printSolution(Graph* graph, int dist[], int parent[], int V, int src, int dest) {
    // if the graph is NULL, return
    if (graph == NULL) {return;}

    // if the distance from source to destination is infinite
    // then there is no path from source to destination
    if (dist[dest] == INT_MAX) {
        printf("No path found from %s to %s\n", graph->array[src].name, graph->array[dest].name);
        return;
    }

    printf("Origin: %s\n", graph->array[src].name);
    printf("Destination: %s\n", graph->array[dest].name);
    printf("Distance: %d\n", dist[dest]);
    printf("Path cities:\n");
    
    printPath(graph, parent, dest);

}

void dijkstra(Graph* graph, int src, int dest) {

    // if the graph is NULL, return
    if (graph == NULL) {return;}

    
    int V = graph->V;

    // The output array. dist[i] will hold the shortest distance from src to i
    int dist[V];
    // sptSet[i] will be true if vertex i is included in shortest path tre
    // or shortest distance from src to i is finalized
    bool sptSet[V];
    // parent array to store the shortest path tree
    int parent[V];

    // Initialize parent of source vertex
    parent[src] = -1;

    // Initialize distances and sptSet
    for (int i = 0; i < V; i++) {
        dist[i] = INT_MAX;
        sptSet[i] = false;
        parent[i] = -1;
    }

    // Distance from source vertex to itself is 0
    dist[src] = 0;

    // do v-1 iterations to find shortest path
    // for all vertices
    for (int count = 0; count < V - 1; count++) {

        // Pick the minimum distance vertex from the set of vertices
        int u = minDistance(dist, sptSet, V);
        // Mark the picked vertex as processed and start from it
        sptSet[u] = true;

        // since we are using adjacency list, we need to iterate through the linked list
        // using pointer temp, not another counter variable, as would be the case with adjacency matrix
        for (AdjListNode* temp = graph->array[u].head; temp != NULL; temp = temp->next) {
            int v = temp->dest;
            // if vertex v is not in sptSet and the distance from source to u is not infinite
            // and the distance from source to v is greater than the distance 
            // from source to u + weight of edge u-v
            // then update the distance from source to v
            if (!sptSet[v] && dist[u] != INT_MAX && dist[u] + temp->weight < dist[v]) {
                parent[v] = u;
                dist[v] = dist[u] + temp->weight;
            }
        }
    }
    // by now, we have the shortest path tree
    // from source to all vertices
    
    // Print the solution
    printSolution(graph, dist, parent, V, src, dest);
}

