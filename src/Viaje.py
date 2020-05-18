# -*- coding: utf-8 -*-
from src.Cars import Hotels
from src.Flights import Flights
from src.User import User
from src.Cars import Cars


class Viaje:

    def __init__(self, user: User, flights: Flights, cars: Cars = None, hotels: Hotels = None):
        self.lista_hoteles = hotels
        self.lista_flights = flights
        self.usuario = user
        self.lista_coches = cars
        pass
