#include "cities.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// takes in the file names for the cities and distances
// reads the files and creates a graph, where we use an adjacency list
// returns the graph
Graph* readCitiesAndCreateGraph(char* fileNameCities, char* fileNameDistances) {
  
    FILE* citiesFile = fopen(fileNameCities, "r");
    FILE* distancesFile = fopen(fileNameDistances, "r");

    if (!citiesFile || !distancesFile) {
        printf("Error opening file\n");
        return NULL;
    }

    int numCities = 0;

    // 25 characters for the city name and 1 for the null terminator \0
    char cityName[26];
    
    while (fscanf(citiesFile, "%s", cityName) == 1) {
        numCities++;
    }

    // create the graph. see adjlist.h for the definition of the Graph struct
    Graph* graph = createGraph(numCities);

    // rewind the file pointer to the beginning of the file
    // so we can read the city names again
    rewind(citiesFile);
    // store city names
    for (int i = 0; i < numCities; i++) {
        fscanf(citiesFile, "%s", graph->array[i].name);
    }

    // store distances
    char cityFromName[26], cityToName[26];
    int distance;
    // scanf returns the number of items read. it can access the number of items read
    // so we can use it to check if we read 3 items
    while (fscanf(distancesFile, "%s %s %d", cityFromName, cityToName, &distance) == 3) {
        // find the index of the source and destination cities
        int src = -1, dest = -1;
        // loop through the graph to find the index of the source and destination cities
        for (int i = 0; i < graph->V; i++) {
            // strcmp returns 0 if the strings are equal
            if (strcmp(graph->array[i].name, cityFromName) == 0) {
                src = i;
            }
            if (strcmp(graph->array[i].name, cityToName) == 0) {
                dest = i;
            }
        }
        // if the city is not found, print an error message and return NULL
        if (src == -1 || dest == -1) {
            printf("Error: city not found\n");
            return NULL;
        }
        // once we have the source and destination city indices, we can add the edge
        addEdge(graph, src, dest, distance);
    }

    fclose(citiesFile);
    fclose(distancesFile);

    return graph;
}
