import json

__author__ = 'Anurag'


class City:
    "Class for saving information about a particular city or metro"

    noOfCities = 0

    def __init__(self,code,name,country,continent,timezone,coordinates,population,region):
        self.code = code
        self.name = name
        self.country = country
        self.continent = continent
        self.timezone = timezone
        self.coordinates = coordinates
        self.population = population
        self.region = region

        # acknowledge instantiation of another object of City
        City.noOfCities += 1

    #constructs dictionary for the cities and returns it
    @staticmethod
    def make_city_dict(json_data):
        dict_of_cities = {}
        for city in json_data['metros']:
            currentCity = City(city['code'],city['name'],city['country'],city['continent'],city['timezone'],city['coordinates'],city['population'],city['region'])
            dict_of_cities[currentCity.code] = currentCity
        return dict_of_cities

    #returns city code for name input
    @staticmethod
    def get_city_code(city_name, dict_of_cities):
        for city_key in dict_of_cities:
            if dict_of_cities[city_key].name.lower() == city_name.lower():
                return city_key
        return 'NA'

    #prints all cities in the dictionary
    @staticmethod
    def print_all_cities(dict_of_cities):
        for city_key in sorted(dict_of_cities):
            print("\n",city_key,"\t",dict_of_cities[city_key].name)


    #returns the name and population of biggest city
    @staticmethod
    def get_biggest_city(dict_of_cities):
        max_population = 0
        biggest_city = ""
        for city_key in dict_of_cities:
            population = dict_of_cities[city_key].population
            if population > max_population:
                max_population = population
                biggest_city = dict_of_cities[city_key].name
        return biggest_city + "\nPopulation: " + str(max_population)

    #returns the name and population of smallest city
    @staticmethod
    def get_smallest_city(dict_of_cities):
        min_population = 99999999
        smallest_city = ""
        for city_key in dict_of_cities:
            population = dict_of_cities[city_key].population
            if population < min_population:
                min_population = population
                smallest_city = dict_of_cities[city_key].name
        return smallest_city + "\nPopulation: " + str(min_population)

    @staticmethod
    def get_average_population(dict_of_cities):
        """
        Returns the average population over all cities in the given dictionary
        :param dict_of_cities:
        :return:
        """
        avg_population =0
        total_no_of_cities = 0
        for city_key in dict_of_cities:
            population = dict_of_cities[city_key].population
            avg_population +=population
            total_no_of_cities +=1
        avg_population = avg_population/total_no_of_cities
        return avg_population


    @staticmethod
    def make_dict_of_continents(dict_of_cities):
        """
        constructs dictionary of all continents and returns it
        :param dict_of_cities:
        :return: dictionary of continents
        """
        dict_of_continents = {}
        for city_key in dict_of_cities:
            continent = dict_of_cities[city_key].continent
            city_name = dict_of_cities[city_key].name
            if continent in dict_of_continents:
                dict_of_continents[continent].append(city_name)
            else:
                dict_of_continents[continent] = [city_name]
        return dict_of_continents

    @staticmethod
    def add_city(dict_of_cities,code,name,country,continent,timezone,coordinates,population,region):
        """
        Adds a new city object to the dictionary of cities
        :param dict_of_cities:
        :param code:
        :param name:
        :param country:
        :param continent:
        :param timezone:
        :param coordinates:
        :param population:
        :param region:
        :return:
        """
        new_city = City(code,name,country,continent,timezone,coordinates,population,region)
        dict_of_cities[new_city.code] = new_city

    @staticmethod
    def remove_city(dict_of_cities, to_delete_city_code):
        """
        Removes a given city from the dictionary of cities
        :param dict_of_cities:
        :param to_delete_city_code:
        :return:
        """
        del dict_of_cities[to_delete_city_code]

