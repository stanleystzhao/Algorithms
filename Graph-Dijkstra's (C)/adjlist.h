#ifndef ADJLIST_H
#define ADJLIST_H

#include <stdbool.h>

// Define a struct to represent a node in the adjacency list
// dest is the destination city index (not name)
// weight is the distance between list city and destination cities
// next is a pointer to the next node in the list
// aka another destination city from the same city on this list
typedef struct AdjListNode {
    int dest;
    int weight;
    struct AdjListNode* next;
} AdjListNode;

// Define a struct to represent an adjacency list
// every list is a 'from' city in the graph
// so we can have a city name for a list
typedef struct {
    AdjListNode* head;
    char name[26];
} AdjList;

// Define a struct to represent a graph
// V is the number of vertices in the graph
// array is an array of adjacency lists (aka cities)
typedef struct {
    int V;
    AdjList* array;
} Graph;


// create a new adjacency list node
// dest is the destination city index (not name)
// weight is the distance between list city and destination cities
AdjListNode* newAdjListNode(int dest, int weight);

// A utility function to create a new adjacency list graph
// with V vertices using an adjacency list representation
Graph* createGraph(int V);

// Function to add an edge to the graph
void addEdge(Graph* graph, int src, int dest, int weight);

// Function to print the adjacency list representation of the graph
void printGraph(Graph* graph);

// Function to free the memory allocated for the graph
void freeGraph(Graph* graph);

#endif