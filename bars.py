import json
from geopy.distance import vincenty


def load_data(filepath):
    with open(filepath, encoding="utf-8") as json_file:
        json_data = json.load(json_file)
    return json_data


def print_biggest_bar(json_data):
    max_seats = max(json_data, key=lambda x: x['SeatsCount'])
    print("The biggest bar is: ", max_seats['Name'])


def print_smallest_bar(json_data):
    min_seats = min(json_data, key=lambda x: x['SeatsCount'])
    print("The smallest bar is: ", min_seats['Name'])


def print_closest_bar(json_data, longitude, latitude):
    bar_coords = json_data[0]['geoData']['coordinates']
    position = (longitude, latitude)
    min_range = vincenty(bar_coords, position).miles
    for bar_cell in json_data:
        bar_coords = bar_cell['geoData']['coordinates']
        range_to_bar = vincenty(bar_coords, position).miles
        if min_range >= range_to_bar:
            min_range = range_to_bar
            closest_bar = bar_cell
    print("The closest bar is: ", closest_bar['Name'])


if __name__ == '__main__':
    filepath_input = input("Enter the file path to JSON: \n")
    data_to_analyse = load_data(filepath_input)
    print("Enter the longitude and latitude:")
    longitude = float(input())
    latitude = float(input())
    get_biggest_bar(data_to_analyse)
    get_smallest_bar(data_to_analyse)
    get_closest_bar(data_to_analyse, longitude, latitude)
