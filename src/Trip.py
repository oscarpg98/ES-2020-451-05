from src.Hotels import Hotels
from src.Flights import Flights
from src.User import User
from src.Cars import Cars


class Trip:

    def __init__(self, user: User):
        self.user = user
        self.hotel_list = []
        self.flight_list = []
        self.car_list = []

    def add_flight(self, flight: Flights):
        self.flight_list.append(flight)

    def add_hotel(self, hotel: Hotels):
        self.hotel_list.append(hotel)

    def add_car(self, car: Cars):
        self.car_list.append(car)

    def get_flights(self):
        return len(self.flight_list)
