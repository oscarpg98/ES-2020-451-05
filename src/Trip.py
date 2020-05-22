from src.Hotels import Hotels
from src.Hotel import Hotel
from src.User import User
from src.Flights import Flights
from src.Flight import Flight
from src.Cars import Cars
from src.Car import Car

IVA = 0.21


class Trip:

    def __init__(self, user: User):
        self.user = user
        self.flights = Flights()
        self.hotels = Hotels()
        self.cars = Cars()
        self.total_price = 0.0

    def get_price_without_iva(self):
        return self.total_price * (1-IVA)

    def get_iva_price(self):
        return self.total_price * IVA

    def get_iva_percentage(self):
        return IVA * 100

    def get_total_price_with_iva(self):
        return self.total_price

    def get_flight_ids(self):
        return self.flights.get_id_list()

    def destination_is_empty(self):
        return self.flights.destination_is_empty()

    def flight_list_is_empty(self):
        return self.flights.flight_list_is_empty()

    def get_destinations(self):
        return self.flights.get_destination_list()

    def add_flight(self, flight: Flight):
        self.flights.add_flight(flight)
        self.total_price = self.flights.get_flights_price()

    def delete_flight(self, flight: Flight):
        self.flights.delete_flight(flight)
        self.total_price = self.flights.get_flights_price()

    def add_hotel(self, hotel: Hotel):
        self.hotels.add_hotel(hotel)
        self.total_price = self.hotels.get_hotels_price()

    def delete_hotel(self, hotel: Hotel):
        self.hotels.delete_hotel(hotel)
        self.total_price = self.hotels.get_hotels_price()

    def add_car(self, car: Car):
        self.cars.add_car(car)
        self.total_price = self.cars.get_cars_price()

    def delete_car(self, car: Car):
        self.cars.delete_car(car)
        self.total_price = self.cars.get_cars_price()

    def confirm_flight_reservation(self, confirmed: bool):
        if confirmed:
            return 'Your flights have been reserved successfully.'
        return 'Your flight reservation has been denied.'

    def confirm_car_reservation(self, confirmed: bool):
        if confirmed:
            return 'Your cars have been reserved successfully.'
        return 'Your car reservation has been denied.'

    def confirm_hotel_reservation(self, confirmed: bool):
        if confirmed:
            return 'Your hotels have been reserved successfully.'
        return 'Your hotel reservation has been denied.'

    def confirm_payment(self, confirmed: bool):
        if confirmed:
            return 'Payment has been done successfully.'
        return 'Payment has been denied.'

    def get_cars(self):
        return self.cars

    def get_flights(self):
        return self.flights

    def get_hotels(self):
        return self.hotels
