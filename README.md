# CSAir
Elaborate implementation of an airline route map and its various features in python.

##Problem Statement

You are a senior software engineer for a new international airline, CSAir. Before CSAir launches passenger service across the globe, they first need to start selling tickets to passengers. But before that can happen, some software needs to be written to manage the extensive route map. You have been tasked by CEO Woodley to begin work on this software. Specifically, the initial requirements for this new software are:
* Parse the raw data that represents CSAir's route map into a data structure in memory
* Allow users of the software to query data about each of the destinations that CSAir flies to, including its code, name, country, continent, timezone, longitude and latitude, population, region, and each of the cities that are accessible via a single non-stop flight from that destination
Provide a graphical representation of CSAir's route map

Your interface should allow the user to:
* Get a list of all the cities that CSAir flies to
* Get specific information about a specific city in the CSAir route network. This information should include:
* Its code
* Its name
* Its country
* Its continent
* Its timezone
* Its latitude and longitude
* Its population
* Its region
* A list of all of the other cities that are accessible via a single non-stop flight from that source city. This list should include the distance of each of those flights.
* Statistical information about CSAir's route network, such as:
* the longest single flight in the network
* the shortest single flight in the network
* the average distance of all the flights in the network
* the biggest city (by population) served by CSAir
* the smallest city (by population) served by CSAir
* the average size (by population) of all the cities served by CSAir
* a list of the continents served by CSAir and which cities are in them
* identifying CSAir's hub cities – the cities that have the most direct connections.
<br>All of this information should be calculated at query time from your graph and not be hard coded into your source. Your program should be console driven, that is it should start up, prompt the user for input, and be able to perform any combination of valid operations without exiting. Also, be careful to check for invalid input. For instance, what happens when a user queries data about a city that CSAir does not fly to?
<br><br>
###New Requirements:
CEO Woodley has decided that in order to continue the development of the company, the software needs to be able to accommodate changes and be useful for travel agents. The new requirements for the software are:
* Allow for online editing of the route network
* Saving the route network back to disk and load new network data
* Displaying additional information about routes in the network
* Allow for finding the shortest route between two cities
