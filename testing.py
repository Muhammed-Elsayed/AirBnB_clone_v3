#!/usr/bin/python3
from models import storage
from models.state import State
from models.city import City

def start():    
	state = "Alabama"
	cities_all = []
	cities = storage.all("City").values()
	for city in cities:
			cities_all.append(city) 

	print(cities_all)


print(start())
