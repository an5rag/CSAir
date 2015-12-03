import webbrowser

from csAir.jsonUtilities import jsonUtility
from csAir.City import City
from csAir.Edge import Edge
from csAir.Graph import make_graph, get_hub_cities, find_shortest_path
from csAir.jsonUtilities.jsonUtility import parse_json, save_to_disk_json, extend_json_data

__author__ = 'Anurag'

def validate_city_name_or_code(city_selected, dict_of_cities):
        """
        Checks if a given City Code or Name exists or not
        :param city_selected: Code or Name of the city
        :param dict_of_cities:
        :return: Returns City Code if found or False if not
        """
        city_selected = city_selected.upper();
        # convert to city code if name is valid
        city_code_from_selected = City.get_city_code(city_selected, dict_of_cities)
        if not city_code_from_selected == 'NA':
            city_selected = city_code_from_selected

        # check if city code exists in the system
        if not city_selected in dict_of_cities:
            print("City does not exist in our system or is not currently served by CSAir")
            return False
        else:
            return city_selected


def handle_city_option(dict_of_edges,dict_of_cities,graph):
        """
        Does all functions  relating to city option
        :param dict_of_edges:
        :param dict_of_cities:
        :param graph:
        :return: Nothing
        """
        print("\n---------------------------------------------\n")
        print("Get Specific City Information")
        print("\n---------------------------------------------\n")
        city_selected = input("Please enter City Code or Name")

        result = validate_city_name_or_code(city_selected, dict_of_cities)
        if not result:
            return
        else:
            city_selected = result

        print("\nCurrent options:")
        print("\n1. Get Code")
        print("\n2. Get Name")
        print("\n3. Get Country")
        print("\n4. Get Continent")
        print("\n5. Get TimeZone")
        print("\n6. Get Coordinates")
        print("\n7. Get Population")
        print("\n8. Get Region")
        print("\n9. Get List of all Accessible Cities")
        print("\n10. Go back to previous menu.")

        city_option = input("\n\nPlease enter the number of your choice: ")

        if not str(city_option).isdigit() or int(city_option)>9 or int(city_option)<1:
            print("Invalid option. Please Try again.")
            input("Press Enter to Continue.")
            return

        if int(city_option)==1:
            print("Code: ", city_selected)
        if int(city_option)==2:
            print("Name: ", dict_of_cities[city_selected].name)
        if int(city_option)==3:
            print("Country: ", dict_of_cities[city_selected].country)
        if int(city_option)==4:
            print("Continent: ", dict_of_cities[city_selected].continent)
        if int(city_option)==5:
            print("TimeZone: ", dict_of_cities[city_selected].timezone)
        if int(city_option)==6:
            print("Coordinates: ", dict_of_cities[city_selected].coordinates)
        if int(city_option)==7:
            print("Population: ", dict_of_cities[city_selected].population)
        if int(city_option)==8:
            print("Region: ", dict_of_cities[city_selected].region)
        if int(city_option)==9:
            print("List of All Accessible Cities: ")
            for accessible_city in graph[city_selected]:
                # accessible is a two element tuple (destination-code,distance)
                print(accessible_city[0])
                print(dict_of_cities[accessible_city[0]].name)
                distance = accessible_city[1]
                print("Distance: ",distance,"\n")
        if int(city_option)==10:
            return



def handle_statistics_option(dict_of_edges, dict_of_cities, graph):
        """
        Handles all statistical queries
        :param dict_of_edges:
        :param dict_of_cities:
        :param graph:
        :return: Nothing
        """
        print("\n---------------------------------------------\n")
        print("Get Statistical Information about our Route Network")
        print("\n---------------------------------------------\n")

        print("\nCurrent options:")
        print("\n1. Get the longest single flight in the network")
        print("\n2. Get the shortest single flight in the network")
        print("\n3. Get the average distance of all the flights in the network")
        print("\n4. Get the biggest city (by population) served by CSAir")
        print("\n5. Get the smallest city (by population) served by CSAir")
        print("\n6. Get the average size (by population) of all the cities served by CSAir")
        print("\n7. Get a list of the continents served by CSAir and which cities are in them")
        print("\n8. Get CSAir's hub cities")

        stat_choice = input("\n\nPlease enter the number of your choice: ")

        if not str(stat_choice).isdigit() or int(stat_choice)>8 or int(stat_choice)<1:
            print("Invalid option. Please Try again.")
            input("Press Enter to Continue.")
            return

        if int(stat_choice) == 1:
            print(Edge.get_longest_flight(dict_of_edges))

        if int(stat_choice) == 2:
            print(Edge.get_shortest_flight(dict_of_edges))

        if int(stat_choice) == 3:
            print("Average Distance: " + str(Edge.get_average_distance(dict_of_edges)))

        if int(stat_choice) == 4:
            print(City.get_biggest_city(dict_of_cities))

        if int(stat_choice) == 5:
            print(City.get_smallest_city(dict_of_cities))

        if int(stat_choice) == 6:
            print("Average Population: " + str(City.get_average_population(dict_of_cities)))

        if int(stat_choice) == 7:
            print(City.make_dict_of_continents(dict_of_cities))


        if int(stat_choice) == 8:
            print("The Hub cities are:")
            hub_cities = get_hub_cities(graph)
            for city in hub_cities:
                print(dict_of_cities[city].name)


def handle_admin_option(json_data, dict_of_edges, dict_of_cities, graph):
    """
    Handles all admin stuff like add, delete, edit city/routes
    :param json_data:
    :param dict_of_edges:
    :param dict_of_cities:
    :param graph:
    :return: Nothing
    """
    print("\n---------------------------------------------\n")
    print("Admin Options")
    print("\n---------------------------------------------\n")
    print("\nCurrent options:")
    print("\n1. Add a City")
    print("\n2. Add a Route")
    print("\n3. Edit a City")
    print("\n4. Remove a City")
    print("\n5. Remove a Route")
    print("\n6. Go back to previous menu")

    admin_choice = input("\n\nPlease enter the number of your choice: ")

    if int(admin_choice) == 1:
        print("ADD A NEW CITY")
        print("---------------")
        code = input("Enter New City Code: (like NYC) ")
        name = input("Enter New City Name: (like New York) ")
        country = input("Enter New City Country: (like US) ")
        continent = input("Enter New City Continent: (like North America) ")
        timezone = input("Enter New City Time Zone: (like -5) ")
        coordinates = input("Enter New City Coordinates: (like {'N'' : 41, 'W' : 74}) ")
        population = input("Enter New City Population: (like 20000000) ")
        region = input("Enter New City Region: (like 3) ")

        if not str(population).isdigit() or int(population) < 0:
            print("Population invalid!")
            return

        # if not str(timezone).isnumeric():
        #     print("TimeZone invalid!")
        #     return

        if not str(region).isdigit() or int(region) < 0:
            print("Region invalid!")
            return

        City.add_city(dict_of_cities,code,name,country,continent,timezone,coordinates,population,region)
        jsonUtility.add_city_to_json_data(json_data,code,name,country,continent,timezone,coordinates,population,region)

    if int(admin_choice) == 2:
        print("ADD A NEW ROUTE")
        print("---------------")

        source = input("Enter Source Code or Name: (like NYC or New York City) ")
        source = validate_city_name_or_code(source, dict_of_cities)
        if not source:
            return

        destination = input("Enter Destination Code or Name: (like LON or London) ")
        destination = validate_city_name_or_code(destination, dict_of_cities)
        if not destination:
            return

        distance = input("Enter Distance (in mi): (like 12345) ")
        if not str(distance).isnumeric() or int(distance) < 0:
            print("Distance invalid!")
            return

        Edge.add_edge(dict_of_edges,source,destination,distance)
        jsonUtility.add_route_to_json_data(json_data,source,destination,distance)

    if int(admin_choice) == 3:
        print("EDIT CITY")
        print("---------------")
        city_to_edit = input("Enter City Code or Name: (like NYC or New York City) ")
        city_to_edit = validate_city_name_or_code(city_to_edit, dict_of_cities)
        if not city_to_edit:
            return
        print("For the following prompts, enter NA if you don't want to change.\n")
        name = input("Enter New City Name: (like New York) ")
        country = input("Enter New City Country: (like US) ")
        continent = input("Enter New City Continent: (like North America) ")
        timezone = input("Enter New City Time Zone: (like -5) ")
        coordinates = input("Enter New City Coordinates: (like {'N'' : 41, 'W' : 74}) ")
        population = input("Enter New City Population: (like 20000000) ")
        region = input("Enter New City Region: (like 3) ")

        city = dict_of_cities[city_to_edit]
        if not name == 'NA':
            city.name = name
        if not country == 'NA':
            city.country = country
        if not continent == 'NA':
            city.continent = continent
        if not timezone == 'NA':
            city.timezone = timezone
        if not coordinates == 'NA':
            city.coordinates = coordinates
        if not population == 'NA':
            city.population = population
        if not region == 'NA':
            city.region = region

        # change things in the json_data - by deleting old city and adding new one
        jsonUtility.delete_city_from_json_data(json_data,city_to_edit)
        jsonUtility.add_city_to_json_data(json_data,city.code,city.name,city.country,city.continent,city.timezone,city.coordinates,city.population,city.region)
        return

    if int(admin_choice) == 4:
        print("REMOVE CITY")
        print("---------------")
        city_to_remove = input("Enter City Code or Name: (like NYC or New York City) ")
        city_to_remove = validate_city_name_or_code(city_to_remove, dict_of_cities)
        if not city_to_remove:
            return
        jsonUtility.delete_city_from_json_data(json_data,city_to_remove)
        Edge.remove_city_edges(dict_of_edges, city_to_remove)
        City.remove_city(dict_of_cities,city_to_remove)

    if int(admin_choice) == 5:
        print("REMOVE ROUTE")
        print("---------------")
        edge_string = input("Enter SourceCode-DestinationCode: (like NYC-LON) ")
        result = Edge.remove_edge(dict_of_edges,edge_string)
        if not result:
            print("Either route format was invalid or route does not exist.")
        else:
            print("Route successfully deleted.")

def handle_route_information_option(dict_of_edges, dict_of_cities, graph):
    """
    Handles queries asking for route information for a given complete route (inputted from the console)
    :param dict_of_edges:
    :param dict_of_cities:
    :param graph:
    :return: Nothing
    """
    print("ROUTE INFORMATION")
    print("------------------")
    print("Enter the subsequent cities and enter 'STOP' when you're done entering.\n")
    locations = []
    current_city = input()
    while not current_city.upper() == 'STOP':

        current_city = validate_city_name_or_code(current_city, dict_of_cities)
        if not current_city:
            return

        locations.append(current_city)
        current_city = input()

    print("Route:- ")
    for city in locations:
        print(city, end = "-->")
    print("||")

    Edge.getRouteInformation(dict_of_edges,graph,locations)

def handle_shortest_path_option(dict_of_edges, dict_of_cities, graph):
    """
    Handles the shortest path option. Calls Graph's get_shortest_path to compute the path
    :param dict_of_edges:
    :param dict_of_cities:
    :param graph:
    :return: Nothing
    """
    source = input("Enter Source City Code or Name: ")

    source = validate_city_name_or_code(source, dict_of_cities)
    if not source:
        return

    destination = input("Enter Destination City Code or Name: ")

    destination = validate_city_name_or_code(destination, dict_of_cities)
    if not destination:
        return

    find_shortest_path(graph,source,destination, dict_of_edges)

# ------------------------------------------------------------------------------------ #
# ---------------------------------MAIN CODE STARTS HERE------------------------------ #
# ------------------------------------------------------------------------------------ #


#parse the json
json_data = parse_json("jsonUtilities/newJson.txt")

#parse the json with Champaign information
extra_json_data_file_name = "jsonUtilities/extra_json.txt"
extend_json_data(json_data,extra_json_data_file_name)

#construct dictionary of edges
dict_of_edges = Edge.make_dict(json_data)

#construct graph
graph = make_graph(dict_of_edges)

#construct dictionary of cities
dict_of_cities = City.make_city_dict(json_data)

#maximum number of options supported
no_of_options = 8
choice = -1


# FOR PRINTING THE GRAPH
# for key in sorted(graph):
#     print(key +" -> "+ str(graph[key]))


#main loop for querying
while int(choice) != 8:
    print("\n---------------------------------------------\n")
    print("Welcome to CSAir Public Information System.")
    print("\n---------------------------------------------\n")
    print("\nCurrent options:")
    print("\n1. Get List of All Served Cities")
    print("\n2. Get Specific City Information")
    print("\n3. Get Statistical Information about our Route Network")
    print("\n4. See Visual Map of all CSAir served Routes")
    print("\n5. Admin-related options")
    print("\n6. Get information about a particular Route")
    print("\n7. Get shortest path between two cities")
    print("\n8. Exit the System")

    choice = input("\n\nPlease enter the number of your choice: ")

    # check for Invalid Option
    if not str(choice).isdigit() or int(choice)>no_of_options or int(choice)<1:
        print("Invalid option. Please Try again.")
        choice = -1
        input("Press Enter to Continue.")
        continue

    # Get List of All Served Cities
    if(int(choice)==1):
        City.print_all_cities(dict_of_cities)

    # Get Specific City Information
    if(int(choice)==2):
        handle_city_option(dict_of_edges,dict_of_cities,graph)

    # Get Statistical Information about our Route Network
    if(int(choice)==3):
        handle_statistics_option(dict_of_edges,dict_of_cities,graph)

    # See Visual Map of all CSAir served Routes
    if(int(choice)==4):
        #constructing the url
        url = "http://www.gcmap.com/mapui?P="
        for edge in dict_of_edges:
            url  = url + "+" + edge + ","
        #opening broswer
        webbrowser.open(url[:-1])

    # Admin-related options
    if(int(choice)==5):
        handle_admin_option(json_data,dict_of_edges,dict_of_cities,graph)
        graph = make_graph(dict_of_edges)

    # Get information about a particular Route
    if(int(choice)==6):
        handle_route_information_option(dict_of_edges,dict_of_cities,graph)

    # Get shortest path between two cities
    if(int(choice)==7):
        handle_shortest_path_option(dict_of_edges,dict_of_cities,graph)

    input("\nPress Enter to Continue.")

    # Exit the System
    if(int(choice)==8):
        save_to_disk_json(json_data,"jsonUtilities/newJson.txt")