import json


__author__ = 'an5ra'


def parse_json(text_file_name):
    with open (text_file_name, "r") as myfile:
        data=myfile.read()
    return json.loads(data)


def save_to_disk_json(json_data, output_file_name):
    with open(output_file_name, 'w+') as outfile:
        json.dump(json_data, outfile)


def extend_json_data(json_data,extra_json_data_file_name):
    extra_json_data = parse_json(extra_json_data_file_name)

    extra_routes_list = extra_json_data["routes"]
    extra_metros_list = extra_json_data["metros"]

    # only add to the existing list if not present earlier
    json_data["routes"].extend(route for route in extra_routes_list if route not in json_data["routes"])
    json_data["metros"].extend(metro for metro in extra_metros_list if metro not in json_data["metros"])


def delete_route_from_json_data(json_data,route_string):
    source_code = route_string[:3]
    destination_code = route_string[4:]
    route_list = json_data["routes"]
    for i in range(len(route_list)):
        source = route_list[i]["ports"][0]
        destination = route_list[i]["ports"][1]
        if source_code==source and destination_code==destination:
            del route_list[i]
            return True
    return False


def delete_city_from_json_data(json_data,city_code_to_delete):
    metros_list = json_data["metros"]
    for i in range(len(metros_list)):
        city_code = metros_list[i]["code"]
        if city_code_to_delete==city_code:
            del metros_list[i]
            return True
    return False

def add_route_to_json_data(json_data,source, destination, distance):

    route_list = json_data["routes"]
    ports = [source, destination]
    new_route = {}
    new_route["ports"] = ports
    new_route["distance"] = distance
    route_list.append(new_route)


def add_city_to_json_data(json_data,code,name,country,continent,timezone,coordinates,population,region):
    metros_list = json_data["metros"]
    new_city = {}
    new_city["code"] = code
    new_city["name"] = name
    new_city["country"] = country
    new_city["continent"] = continent
    new_city["timezone"] = timezone
    new_city["coordinates"] = coordinates
    new_city["population"] = population
    new_city["region"]  = region
    metros_list.append(new_city)
