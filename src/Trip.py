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
        self.destination_list = []
        self.total_price = 0.0

    def get_flights_len(self):
        return len(self.flight_list)

    def get_destinations_len(self):
        return len(self.destination_list)

    def get_total_price(self):
        return self.total_price

    def get_destinations(self):
        return self.destination_list

    def add_flight(self, flight: Flights):
        self.flight_list.append(flight)
        self.destination_list.append(flight.get_destination())
        self.total_price += (flight.get_price()*float(flight.get_passenger_num()))

    def add_hotel(self, hotel: Hotels):
        self.hotel_list.append(hotel)
        self.total_price += hotel.get_price()

    def add_car(self, car: Cars):
        self.car_list.append(car)
        self.total_price += car.get_price()

    def delete_flight(self, flight: Flights):
        self.total_price -= (flight.get_price()*float(flight.get_passenger_num()))
        dest = flight.get_destination()
        self.flight_list.remove(flight)
        self.destination_list.remove(dest)

    def destination_is_empty(self) -> bool:
        n = len(self.destination_list)
        if n == 0:
            return True
        return False

    def flight_list_is_empty(self) -> bool:
        n = len(self.flight_list)
        if n == 0:
            return True
        return False


