from lists import get_list_of_citites, get_list_of_places

class city_info:
	def __init__(self):
		pass


def get_places(city_name):
	list_of_citites = get_list_of_citites()
	list_of_places = get_list_of_places()
	list_of_places_per_city = {list_of_cities[index]: [] for index in range(len(list_of_cities))}
