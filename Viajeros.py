# -*- coding: utf-8 -*-
import Hotels 
import Flights
import User
import Cars

class Viajeros:
    
    def __init__(self, user:User, flights:Flights, cars:Cars=None, hotels:Hotels=None):
        self.lista_hoteles = hotels
        self.lista_flights = flights
        self.usuario = user
        self.lista_coches = cars        
        pass
