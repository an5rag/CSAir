import json
from queue import Queue, PriorityQueue
from csAir.Edge import Edge

__author__ = 'Anurag'


def make_graph(dict_of_edges):
    """
    Constructs the graph out of a dictionary of edges
    :param dict_of_edges:
    :return: the graph itself
    """
    graph = {}
    for edge in dict_of_edges:
        source = dict_of_edges[edge].sourceCode
        destination = dict_of_edges[edge].destinationCode
        distance = dict_of_edges[edge].distance
        if source in graph:
            graph[source].append((destination,distance))
        else:
            graph[source] = [(destination,distance)]
    return graph

def get_hub_cities(graph):
    """
    Finds those cities with maximum number of outgoing edges, hence Hub-cities
    :param graph:
    :return:
    """
    max_connections = 0
    hub_cities = []
    # Finding the maximum number of connections
    for source in graph:
        no_of_connections  = len(graph[source])
        if no_of_connections>max_connections:
            max_connections = no_of_connections

    # Finding all cities having that number of connections
    for source in graph:
        no_of_connections  = len(graph[source])
        if no_of_connections == max_connections:
            hub_cities.append(source)

    return hub_cities

def print_graph(graph):
    """
    Formatted printing of the graph
    :param graph:
    :return:
    """
    for source in sorted(graph):
        print(source + "->" + str(graph[source]))


def find_shortest_path(graph, source, destination, dict_of_edges):
    """
    Uses DIJKSTRA'S ALGORITHM TO GET THE SHORTEST PATH
    :param graph:
    :param source:
    :param destination:
    :param dict_of_edges: to later find out the route information
    :return:
    """
    dist = {}
    prev = {}
    unvisited = []
    found = False
    for key in graph:
        dist[key] = 999999
        prev[key] = "NA"
        unvisited.append(key)

    dist[source] = 0

    while len(unvisited) > 0:
        u = unvisited[0]
        for city in unvisited:
            if dist[city]<dist[u]:
                u = city
        unvisited.remove(u)
        if u==destination:
            found = True
            break

        for neighbour in graph[u]:
            neighbour_key = neighbour[0]
            neighbour_distance = neighbour[1]
            alt = dist[u] + neighbour_distance
            if alt < dist[neighbour_key]:
                dist[neighbour_key] = alt
                prev[neighbour_key] = u
    stack_of_path = []
    if found:
        previous = destination
        while not previous == source:
            stack_of_path.append(previous)
            # print(previous, end  = "<--")
            previous = prev[previous]
    else:
        print("No path between ends found!")

    if found:
        locations = []
        stack_of_path.append(source)
        print("\nShortest path is:\n")
        while len(stack_of_path) > 1:
            city_reached = stack_of_path.pop()
            print(city_reached, end="-->")
            locations.append(city_reached)
        print(destination)
        locations.append((destination))
        Edge.getRouteInformation(dict_of_edges,graph,locations)