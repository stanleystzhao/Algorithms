#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdbool.h>

#include "cities.h"
#include "dijkstra.h"


/**
 * Main program
 */
int main(int argc, char* argv[]) {

    char* cityfile = "./data/cities1.dat";
    char* distancefile = "./data/distances1.dat";
    char* cityFrom = NULL;
    char* cityTo = NULL;

    // This code is provided to read the command line arguments
    for (int i = 1; i < argc; i++) {
        if (strcmp(argv[i], "-f") == 0) {
            if (i + 1 < argc) {
                cityFrom = argv[++i];
            } else {
                printf("Missing argument for -f\n");
                return 1;
            }
        } else if (strcmp(argv[i], "-t") == 0) {
            if (i + 1 < argc) {
                cityTo = argv[++i];
            } else {
                printf("Missing argument for -t\n");
                return 1;
            }
        } else {
            printf("Unknown argument: %s\n", argv[i]);
            return 1;
        }
    }

    if ( !cityFrom || !cityTo) {
        printf("Usage: %s -f <city_from> -t <city_to>\n", argv[0]);
        return 1;
    }

    // your code here

    // Read the cities and distances from the files
    // And create the graph
    Graph* graph = readCitiesAndCreateGraph(cityfile, distancefile);
    if (!graph) {
        printf("Error creating graph\n");
        return 1;
    }

    // initialize the source and destination city indices as -1
    // becasue no index is -1
    // then we will search for the source and destination cities
    int src = -1, dest = -1;
    for (int i = 0; i < graph->V; i++) {
        if (strcmp(graph->array[i].name, cityFrom) == 0) {
            src = i;
        }
        if (strcmp(graph->array[i].name, cityTo) == 0) {
            dest = i;
        }
    }

    // If the source or destination city is not found
    // in the graph, print an error message and return
    if (src == -1 || dest == -1) {
        printf("City not found in the graph\n");
        return 1;
    }

    // Find the shortest path
    // we will print the path in the dijkstra function
    // so we don't need to print it here
    // see dijkstra.c
    dijkstra(graph, src, dest);

    // Free the graph
    freeGraph(graph);
    
    return 0;
}