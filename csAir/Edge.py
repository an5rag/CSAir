import json
from math import sqrt

__author__ = 'an5ra'

class Edge:
    "Class to define an object of Edge and its various properties"

    noOfEdges = 0

    def __init__(self, sourceCode, destinationCode, distance):
        self.sourceCode = sourceCode
        self.destinationCode =destinationCode
        self.distance = distance

        # acknowledge instantiation of another object of Edge
        Edge.noOfEdges += 1

    def __str__(self):
        return "\nSource: "+self.sourceCode+"\nDestination: "+self.destinationCode+"\nDistance: "+str(self.distance)

    def __repr__(self):
        return str(self)

    @staticmethod
    def make_dict(jsonData):
        """
        Makes a Dictionary of Edges using the JSon Data that is passed to it
        :param jsonData:
        :return: the dict itself
        """
        dict_of_edges = {}
        for edge in jsonData['routes']:
            # adding source-to-destination edge
            source = edge['ports'][0]
            destination = edge['ports'][1]
            distance = edge['distance']
            currentEdge = Edge(source,destination,distance)
            dict_of_edges[source + "-" + destination] = currentEdge

            #adding destination-to-source edge
            source = edge['ports'][1]
            destination = edge['ports'][0]
            distance = edge['distance']
            currentEdge = Edge(source,destination,distance)
            dict_of_edges[source + "-" + destination] = currentEdge

        return dict_of_edges

    @staticmethod
    def get_longest_flight(dict_of_edges):
        """
        Returns a String with information of the longest flight
        :param dict_of_edges:
        :return: the result string
        """
        max_distance = 0
        max_edge = ""
        for edge in dict_of_edges:
            distance = dict_of_edges[edge].distance
            if distance>max_distance:
                max_distance = distance
                max_edge = edge
        return str(max_edge)+"\n"+"Distance: "+str(max_distance)

    @staticmethod
    def get_shortest_flight(dict_of_edges):
        """
        Returns a String with information of the shortest flight
        :param dict_of_edges:
        :return:
        """
        min_distance = 99999999
        min_edge = ""
        for edge in dict_of_edges:
            distance = dict_of_edges[edge].distance
            if distance<min_distance:
                min_distance = distance
                min_edge = edge
        return str(min_edge)+"\n"+"Distance: "+str(min_distance)

    @staticmethod
    def get_average_distance(dict_of_edges):
        """
        Returns the average distance across all routes
        :param dict_of_edges:
        :return:
        """
        avg_distance = 0
        total_no_of_edges = 0
        for edge in dict_of_edges:
            distance = dict_of_edges[edge].distance
            avg_distance +=distance
            total_no_of_edges +=1
        avg_distance = avg_distance/total_no_of_edges
        return avg_distance

    @staticmethod
    def remove_city_edges(dict_of_edges,city_code):
        """
        Removes all edges in the dictionary argument with either source or destination as the city_code
        :param dict_of_edges:
        :param city_code:
        :return:
        """

        deletion_list = []
        for edge in dict_of_edges:
            source = edge[:3]
            destination = edge[4:]
            if source == city_code or destination == city_code:
                deletion_list.append(edge)

        for edge in deletion_list:
            del dict_of_edges[edge]


    @staticmethod
    def remove_edge(dict_of_edges,edge_string):
        """
        Removes the given route from the edge dictionary
        :param dict_of_edges:
        :param edge_string:
        :return:
        """
        if edge_string in dict_of_edges:
            del dict_of_edges[edge_string]
            return True
        else:
            return False

    @staticmethod
    def add_edge(dict_of_edges, source, destination, distance):
        """
        Adds an edge to the dictionary
        :param dict_of_edges:
        :param source:
        :param destination:
        :param distance:
        :return:
        """
        currentEdge = Edge(source,destination,distance)
        dict_of_edges[source + "-" + destination] = currentEdge

    @staticmethod
    def getRouteInformation(dict_of_edges, graph, locations):
        """
        Prints the time, cost and distance over a given (valid) collection of routes
        :param dict_of_edges:
        :param graph:
        :param locations:
        :return: a tuple of (total_distance, total_time, total_cost)
        """
        total_time = 0
        total_layover = 0
        total_cost = 0
        total_distance = 0
        starting_cost_per_km = 0.35
        source = locations[0]
        previous_location = source
        last_layover = 0

        for i in range(1,len(locations)):
            current_route = previous_location+"-"+locations[i]

            # ----------- Checking if connection exists ---------
            if current_route not in dict_of_edges:
                print("Invalid connection at " + current_route)
                return

            # ------------ Calculating current distance --------------
            current_distance = dict_of_edges[current_route].distance
            total_distance += current_distance

            # ------------ Calculating current time -----------------

            if(current_distance>400):
               time_to_accelerate = 40/75  # pre-computed value
               current_time = (current_distance-400)/750 + time_to_accelerate*2
            else:
                acceleration_distance = current_distance/2
                acceleration = (75*75)/40  # pre-computed value
                current_time = sqrt(2*acceleration_distance/acceleration)

            total_time += current_time

            # ------------ Calculating current layover --------------
            number_of_outbound_flights = len(graph[source])
            current_layover = 120 - 10*(number_of_outbound_flights-1)
            if current_layover < 0:
                current_layover = 0
            total_layover += current_layover
            last_layover = current_layover  # keeping track of last layover

            # ------------ Calculating current cost -----------------
            current_cost = (starting_cost_per_km - 0.05*(i-1)) * current_distance
            if(current_cost<0):
                current_cost=0
            total_cost += current_cost
            # ---------------------------------------------------------

            previous_location = locations[i]  # keeping track of previous location

        total_time += (total_layover - last_layover)/60
        hours = int(total_time)
        minutes = int((total_time - hours)*60)

        print("Total distance: ",total_distance, " km")
        print("Total time: ", hours, " hours and ",minutes, " minutes" )
        print("Total cost: $", total_cost)

        return (total_distance, total_time, total_cost)

