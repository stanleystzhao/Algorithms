# Bruce A. Maxwell
# Framework for DFS and Dijkstra's algorithms
# includes a main test function
# Stanley (Shitai) Zhao
# June 14, 2024 (Hawaii Time)
# HW #4


# import the PQ heap and the Node class
from simple_heap import PQ
from simple_graph import Node


# comparison function for the PQ for Dijkstra's algorithm
def pqcompare( a, b ):
    return a._cost < b._cost


# global variable step
step = 0


# DFS explore function
def explore( graph, node ):
    global step
    # set node as visited
    node.setVisited(True)
    # set node's pre field to be step
    node.setPre(step)
    # increment step
    step+=1
    # for each neighbor n of node
    for n in node.neighbors():

        # if n is not visited
        if n.visited() is False:
            # set the parent of n to be node
            n.setParent(node)
            # explore n
            explore(graph, n)
    # set node's post value to be step
    node.setPost(step)
    # increment step
    step+=1
    # print out the node ID, pre/post, and parent ID
    parentid = -1
    if node.parent() != None:
        parentid = node.parent().id()
    print("Node %d (pre, post): (%d, %d)  parent %d" % (node.id(), node.pre(), node.post(), parentid) )

    return


# Executes Depth-First-Search on the graph, visiting all nodes
# Fills out a parent link and pre/post values for each node
def dfs( graph ):
    # initialize the graph
    global step
    step = 1
    # for all nodes n in the graph
    for n in graph:
        # if n is not visited, explore n
        if not n.visited():
            explore(graph, n)

    return


# Implementation of Dijkstra's algorithm
# Takes in a graph (array of Node) and a root node
# Fills out the parent, visited, and cost fields of the graph nodes
def dijkstra(graph, root):

    # create a PQ big enough to hold extras, use pqcompare as the comparison function
    pq = PQ(len(graph)+1, pqcompare)
    # initialize all of the nodes
    for node in graph:
        node.setVisited(False)
        # set initial cost to infinity
        node.setCost(float("inf"))
        node.setParent(None)
    # initialize the source node to 0 cost
    root.setCost(0)
    # add the source node to the priority queue
    pq.add(root)

    # loop
    while not pq.empty():
        # take the next node n off the queue
        n = pq.remove()
        # mark it as visited
        n.setVisited(True)

        # for each neighbor u of n
        for u in n.neighbors():
            # calculate the updated cost from n to u
            current_cost = n.cost() + n.distance(u)
            # if the updated cost is smaller than n's cost
            if current_cost < u.cost():
                # set the cost to the smaller value
                u.setCost(current_cost)
                # set the parent of n to be u
                u.setParent(n)
                # add u to the PQ
                pq.add(u)
    return

    
# Main test function
def main():

    # build a graph, which is a list of Node objects
    graph = []

    graph.append( Node(0, 100, 100) )
    graph.append( Node(1, 200,  20) )
    graph.append( Node(2, 750, 100) )
    graph.append( Node(3, 550, 150) )
    graph.append( Node(4, 400, 250) )
    graph.append( Node(5, 850, 400) )
    graph.append( Node(6, 200, 350) )
    graph.append( Node(7, 550, 450) )
    graph.append( Node(8, 350, 550) )
    graph.append( Node(9, 120, 600) )

    graph[0].addUndirectedNeighbor( graph[1] )
    graph[0].addUndirectedNeighbor( graph[6] )
    graph[1].addUndirectedNeighbor( graph[2] )
    graph[1].addUndirectedNeighbor( graph[4] )
    graph[2].addUndirectedNeighbor( graph[5] )
    graph[2].addUndirectedNeighbor( graph[3] )
    graph[3].addUndirectedNeighbor( graph[5] )
    graph[3].addUndirectedNeighbor( graph[4] )
    graph[3].addUndirectedNeighbor( graph[7] )
    graph[4].addUndirectedNeighbor( graph[6] )
    graph[6].addUndirectedNeighbor( graph[7] )
    graph[6].addUndirectedNeighbor( graph[8] )
    graph[6].addUndirectedNeighbor( graph[9] )
    graph[7].addUndirectedNeighbor( graph[8] )
    graph[8].addUndirectedNeighbor( graph[9] )

    # print the nodes in the graph and each adjacency list
    print("Graph:")
    for node in graph:
        s = "["
        for n in node.neighbors():
            s += str(n) + ", "
        s += "]"
        print(node, s)

    # run DFS and print the search tree information
    print("\nDFS Results")
    dfs(graph)

    # run dijkstra's algorithm with 0 as the root
    dijkstra(graph, graph[0])

    # print the results
    print("\nDijkstra's Results:")
    for node in graph:
        print(node)
            

if __name__ == "__main__":
    main()

