from src.Hotels import Hotels
from src.Hotel import Hotel
from src.User import User
from src.Flights import Flights
from src.Flight import Flight
from src.Cars import Cars
from src.Car import Car
from src.Bank import Bank
from src.PaymentData import PaymentData
from src.Skyscanner import Skyscanner
from src.Rentalcars import Rentalcars
from src.Booking import Booking


class Trip:

    def __init__(self, user: User):
        self.user = user
        self.flights = Flights()
        self.hotels = Hotels()
        self.cars = Cars()
        self.total_price = 0.0

    def get_flight_ids(self):
        return self.flights.get_id_list()

    def destination_is_empty(self):
        return self.flights.destination_is_empty()

    def flight_list_is_empty(self):
        return self.flights.flight_list_is_empty()

    def get_total_price(self):
        return self.total_price

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

    def confirm_flight_reservation(self, user: User):
        sky = Skyscanner()
        if sky.confirm_reserve(user, self.flights):
            return 'Your flights have been reserved successfully.'
        return 'Your flight reservation has been denied.'

    def confirm_car_reservation(self, user: User):
        rent = Rentalcars()
        if rent.confirm_reserve(user, self.cars):
            return 'Your cars have been reserved successfully.'
        return 'Your car reservation has been denied.'

    def confirm_hotel_reservation(self, user: User):
        book = Booking()
        if book.confirm_reserve(user, self.hotels):
            return 'Your hotels have been reserved successfully.'
        return 'Your hotel reservation has been denied.'

    @staticmethod
    def do_payment(user: User, payment: PaymentData):
        bank = Bank()
        if bank.do_payment(user, payment):
            return 'Payment has been done successfully.'
        return 'Payment has been denied.'

    def get_cars(self):
        return self.cars

    def get_flights(self):
        return self.flights

    def get_hotels(self):
        return self.hotels

