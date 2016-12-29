import json
from geopy.distance import vincenty


def load_data(filepath):
    with open(filepath, encoding="utf-8") as json_file:
        json_data = json.load(json_file)
    return json_data


def get_biggest_bar(json_data):
    max_seats = max(json_data, key=lambda x: x['SeatsCount'])
    return max_seats


def get_smallest_bar(json_data):
    min_seats = min(json_data, key=lambda x: x['SeatsCount'])
    return min_seats


def get_closest_bar(json_data, longitude, latitude):
    position = (longitude, latitude)
    closest_bar = min(json_data, key=lambda x: vincenty(x['geoData']['coordinates'], position).miles)
    return closest_bar


def print_bars(biggest_bar, smallest_bar, closest_bar):
    print("The biggest bar is: ", biggest_bar['Name'])
    print("The smallest bar is: ", smallest_bar['Name'])
    print("The closest bar is: ", closest_bar['Name'])


if __name__ == '__main__':
    filepath_input = input("Enter the file path to JSON: \n")
    data_to_analyse = load_data(filepath_input)
    print("Enter the longitude and latitude:")
    longitude = float(input())
    latitude = float(input())
    biggest_bar = get_biggest_bar(data_to_analyse)
    smallest_bar = get_smallest_bar(data_to_analyse)
    closest_bar = get_closest_bar(data_to_analyse, longitude, latitude)
    print_bars(biggest_bar, smallest_bar, closest_bar)
