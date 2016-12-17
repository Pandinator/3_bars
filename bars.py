import json


def load_data(filepath):
    with open(filepath, encoding="UTF-8") as json_file:
    	json_data = json.load(json_file)
    return json_data


def get_biggest_bar(json_data):
    max_seats = json_data[0]['SeatsCount']
    index = 0
    for bar_cell in range(1, len(json_data)):
    	if max_seats < json_data[bar_cell]['SeatsCount']:
    		max_seats = json_data[bar_cell]['SeatsCount']
    		index = bar_cell
    print(json_data[index]['Name'])


def get_smallest_bar(json_data):
    min_seats = json_data[0]['SeatsCount']
    index = 0
    for bar_cell in range(1, len(json_data)):
    	if min_seats > json_data[bar_cell]['SeatsCount']:
    		min_seats = json_data[bar_cell]['SeatsCount']
    		index = bar_cell
    print(json_data[index]['Name'])


def get_closest_bar(json_data, longitude, latitude):
    pass


if __name__ == '__main__':
    filepath_input = input("Enter the file path to JSON: \n")
    data_to_analyse = load_data(filepath_input)
    longitude, latitude = float(input("Enter the longitude and latitude: \n"))
    get_biggest_bar(data_to_analyse)
    get_smallest_bar(data_to_analyse)
