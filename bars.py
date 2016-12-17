import json
from geopy.distance import vincenty


def load_data(filepath):
    with open(filepath, encoding="UTF-8") as json_file:
    	json_data = json.load(json_file)
    return json_data


def get_biggest_bar(json_data):
    max_seats = json_data[0]['SeatsCount']
    for bar_cell in range(1, len(json_data)):
    	if max_seats < json_data[bar_cell]['SeatsCount']:
    		max_seats = json_data[bar_cell]['SeatsCount']
    		index_of_bar = bar_cell
    print("The biggest bar is: ", json_data[index_of_bar]['Name'])


def get_smallest_bar(json_data):
    min_seats = json_data[0]['SeatsCount']
    for bar_cell in range(1, len(json_data)):
    	if min_seats > json_data[bar_cell]['SeatsCount']:
    		min_seats = json_data[bar_cell]['SeatsCount']
    		index_of_bar = bar_cell
    print("The smallest bar is: ", json_data[index_of_bar]['Name'])


def get_closest_bar(json_data, longitude, latitude):
    bar_coords = json_data[0]['geoData']['coordinates']
    position = (longitude, latitude)
    min_range = vincenty(bar_coords, position).miles
    for bar_cell in range(1, len(json_data)):
        bar_coords = json_data[bar_cell]['geoData']['coordinates']
        range_to_bar = vincenty(bar_coords, position).miles
        if min_range >= range_to_bar:
            min_range = range_to_bar
            index_of_bar = bar_cell
    print("The closest bar is: ", json_data[index_of_bar]['Name'])


if __name__ == '__main__':
    filepath_input = input("Enter the file path to JSON: \n")
    data_to_analyse = load_data(filepath_input)
    print("Enter the longitude and latitude:")
    longitude = float(input())
    latitude = float(input())
    get_biggest_bar(data_to_analyse)
    get_smallest_bar(data_to_analyse)
    get_closest_bar(data_to_analyse, longitude, latitude)
