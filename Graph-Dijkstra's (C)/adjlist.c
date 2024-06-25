#include "adjlist.h"
#include <stdio.h>
#include <stdlib.h>


AdjListNode* newAdjListNode(int dest, int weight) {

    AdjListNode* newNode = (AdjListNode*)malloc(sizeof(AdjListNode));

    // if malloc fails, return NULL
    if (!newNode) {
        return NULL;
    }

    newNode->dest = dest;
    newNode->weight = weight;
    // next is a pointer to the next adjacent city of the list head city
    newNode->next = NULL;
    return newNode;
}


Graph* createGraph(int V) {

    Graph* graph = (Graph*)malloc(sizeof(Graph));
    if (!graph) {
        return NULL;
    }

    graph->V = V;

    graph->array = (AdjList*)malloc(V * sizeof(AdjList));
    if (!graph->array) {
        return NULL;
    }

    // initialize each adjacency list as empty by making head as NULL
    for (int i = 0; i < V; ++i) {
        graph->array[i].head = NULL;
        // initialize the name of the city to an empty string
        graph->array[i].name[0] = '\0';
    }

    return graph;

}

void addEdge(Graph* graph, int src, int dest, int weight) {

    AdjListNode* newNode = newAdjListNode(dest, weight);
    if (!newNode) {
        return;
    }

    // add the new node to the beginning of the list
    newNode->next = graph->array[src].head;
    graph->array[src].head = newNode;

}

void printGraph(Graph* graph) {

    // use ++V instead of V++ to avoid the warning
    // "value computed is not used"
    // because we are not using the value of V
    // we are just incrementing it
    for (int v = 0; v < graph->V; ++v) {
        
        AdjListNode* temp = graph->array[v].head;
        
        printf("\n Adjacency list of vertex %d %s\n head ",
        v, graph->array[v].name);
        // while there are nodes in the list
        while (temp) {
            // print the destination city index and the weight
            printf("-> %d(weight:%d) ", temp->dest, temp->weight);
            temp = temp->next;
        }
        printf("\n");
    }
}

void freeGraph(Graph* graph) {
    
    // 1. free each node in the adjacency lists
    for (int i = 0; i < graph->V; i++) {
        AdjListNode* current = graph->array[i].head;
        // while there are nodes in the list
        while (current) {
            // beware of the order of the next three lines
            // if you free the node first,
            // you will lose the reference to the next node
            AdjListNode* next = current->next;
            free(current);
            current = next;
        }
    }
    
    // 2. free the array of adjacency lists   
    free(graph->array);

    // 3. free the graph itself
    free(graph);

}

