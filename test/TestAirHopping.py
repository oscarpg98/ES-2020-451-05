from src.User import User
from src.Trip import Trip
from src.Flight import Flight
from src.Hotel import Hotel
from src.Car import Car
from src.PaymentData import PaymentData
from src.Bank import Bank
from src.Skyscanner import Skyscanner
from src.Booking import Booking
from src.Rentalcars import Rentalcars
from unittest import mock
import unittest

'''
@pytest.fixture()
def user(self):
    user = User('Fariseo', '1234567', 'Serranos', '65612648', 'hola@adios.com')
    return user


@pytest.fixture()
def flight1(self):
    flight = Flight('abc', 4, 'Paris', 'Barcelona', 99.99)
    return flight


@pytest.fixture()
def flight2(self):
    flight = Flight('def', 4, 'Barcelona', 'New York', 399.99)
    return flight


@pytest.fixture()
def flight3(self):
    flight = Flight('ghi', 4, 'New York', 'Paris', 299.99)
    return flight


@pytest.fixture()
def trip1(self):
    user = User('Fariseo', '1234567', 'Serranos', '65612648', 'hola@adios.com')
    flight1 = Flight('abc', 4, 'Paris', 'Barcelona', 99.99)
    flight2 = Flight('def', 4, 'Barcelona', 'New York', 399.99)
    flight3 = Flight('ghi', 4, 'New York', 'Paris', 299.99)
    trip = Trip(user)
    trip.add_flight(flight1)
    trip.add_flight(flight2)
    trip.add_flight(flight3)
    return trip
'''


class TestAirHopping(unittest.TestCase):

    # ------------------------------------------------ Tests Version 1 ------------------------------------------------

    def test_expected_passengers(self):
        flight = Flight('abc', 2, 'Paris', 'Barcelona', 99.99)
        self.assertEqual(2, flight.get_passenger_num())

    def test_empty_destination_list(self):
        user = User('Fariseo', '1234567', 'Serranos', '65612648', 'hola@adios.com')
        trip = Trip(user)
        self.assertEqual(True, trip.destination_is_empty())

    def test_empty_flight_list(self):
        user = User('Fariseo', '1234567', 'Serranos', '65612648', 'hola@adios.com')
        trip = Trip(user)
        self.assertEqual(True, trip.flight_list_is_empty())

    def test_price_no_destinations(self):
        user = User('Fariseo', '1234567', 'Serranos', '65612648', 'hola@adios.com')
        trip = Trip(user)
        self.assertEqual(0.0, trip.get_total_price_with_iva())

    def test_add_destination_list(self):
        user = User('Fariseo', '1234567', 'Serranos', '65612648', 'hola@adios.com')
        flight = Flight('abc', 2, 'Paris', 'Barcelona', 99.99)
        flight2 = Flight('def', 2, 'Barcelona', 'New York', 399.99)
        trip = Trip(user)
        trip.add_flight(flight)
        trip.add_flight(flight2)
        self.assertEqual(['Barcelona', 'New York'], trip.get_destinations())

    def test_add_flight_list(self):
        user = User('Fariseo', '1234567', 'Serranos', '65612648', 'hola@adios.com')
        flight = Flight('abc', 4, 'Paris', 'Barcelona', 99.99)
        flight2 = Flight('def', 4, 'Barcelona', 'New York', 399.99)
        trip = Trip(user)
        trip.add_flight(flight)
        trip.add_flight(flight2)
        self.assertEqual(['abc', 'def'], trip.get_flight_ids())

    def test_price_1_passenger(self):
        user = User('Fariseo', '1234567', 'Serranos', '65612648', 'hola@adios.com')
        flight = Flight('abc', 1, 'Paris', 'Barcelona', 99.99)
        flight2 = Flight('def', 1, 'Barcelona', 'New York', 399.99)
        trip = Trip(user)
        trip.add_flight(flight)
        trip.add_flight(flight2)
        self.assertEqual(499.98, trip.get_total_price_with_iva())

    def test_price_multiple_passengers(self):
        user = User('Fariseo', '1234567', 'Serranos', '65612648', 'hola@adios.com')
        flight = Flight('abc', 2, 'Paris', 'Barcelona', 99.99)
        flight2 = Flight('def', 2, 'Barcelona', 'New York', 399.99)
        trip = Trip(user)
        trip.add_flight(flight)
        trip.add_flight(flight2)
        self.assertEqual(999.96, trip.get_total_price_with_iva())

    def test_dest_list_deleting_dest(self):
        user = User('Fariseo', '1234567', 'Serranos', '65612648', 'hola@adios.com')
        flight = Flight('abc', 2, 'Paris', 'Barcelona', 99.99)
        flight2 = Flight('def', 2, 'Barcelona', 'New York', 399.99)
        trip = Trip(user)
        trip.add_flight(flight)
        trip.add_flight(flight2)
        trip.delete_flight(flight)
        self.assertEqual(['New York'], trip.get_destinations())

    def test_flight_list_deleting_dest(self):
        user = User('Fariseo', '1234567', 'Serranos', '65612648', 'hola@adios.com')
        flight = Flight('abc', 2, 'Paris', 'Barcelona', 99.99)
        flight2 = Flight('def', 2, 'Barcelona', 'New York', 399.99)
        trip = Trip(user)
        trip.add_flight(flight)
        trip.add_flight(flight2)
        trip.delete_flight(flight)
        self.assertEqual(['def'], trip.get_flight_ids())

    def test_price_deleting_dest(self):
        user = User('Fariseo', '1234567', 'Serranos', '65612648', 'hola@adios.com')
        flight = Flight('abc', 4, 'Paris', 'Barcelona', 99.99)
        flight2 = Flight('def', 4, 'Barcelona', 'New York', 399.99)
        flight3 = Flight('ghi', 4, 'New York', 'Paris', 299.99)
        trip = Trip(user)
        trip.add_flight(flight)
        trip.add_flight(flight2)
        trip.add_flight(flight3)
        trip.delete_flight(flight3)
        self.assertEqual(1999.92, trip.get_total_price_with_iva())

    def test_payment_done(self):
        user = User('Fariseo', '1234567', 'Serranos', '65612648', 'hola@adios.com')
        flight = Flight('abc', 4, 'Paris', 'Barcelona', 99.99)
        flight2 = Flight('def', 4, 'Barcelona', 'New York', 399.99)
        flight3 = Flight('ghi', 4, 'New York', 'Paris', 299.99)
        trip = Trip(user)
        trip.add_flight(flight)
        trip.add_flight(flight2)
        trip.add_flight(flight3)
        total_price = trip.get_total_price_with_iva()
        payment = PaymentData('Visa', 'Fariseo', '6456456454', '654', total_price)
        bank = Bank()
        res = bank.do_payment(user, payment)
        confirmed = trip.confirm_payment(res)
        self.assertEqual('Payment has been done successfully.', confirmed)

    def test_flight_reservation(self):
        user = User('Fariseo', '1234567', 'Serranos', '65612648', 'hola@adios.com')
        flight = Flight('abc', 4, 'Paris', 'Barcelona', 99.99)
        flight2 = Flight('def', 4, 'Barcelona', 'New York', 399.99)
        flight3 = Flight('ghi', 4, 'New York', 'Paris', 299.99)
        trip = Trip(user)
        trip.add_flight(flight)
        trip.add_flight(flight2)
        trip.add_flight(flight3)
        flights = trip.get_flights()
        sky = Skyscanner()
        res = sky.confirm_reserve(user, flights)
        confirmed = trip.confirm_flight_reservation(res)
        self.assertEqual('Your flights have been reserved successfully.', confirmed)

    # ------------------------------------------------ Tests Version 2 ------------------------------------------------

    def test_payment_method(self):
        user = User('Fariseo', '1234567', 'Serranos', '65612648', 'hola@adios.com')
        flight = Flight('abc', 4, 'Paris', 'Barcelona', 99.99)
        flight2 = Flight('def', 4, 'Barcelona', 'New York', 399.99)
        trip = Trip(user)
        trip.add_flight(flight)
        trip.add_flight(flight2)
        total_price = trip.get_total_price_with_iva()
        payment = PaymentData('Visa', 'Fariseo', '6456456454', '654', total_price)
        bank = Bank()
        bank.do_payment(user, payment)
        self.assertEqual('Visa', payment.get_card_type())

    @mock.patch('src.Bank')
    def test_payment_denied(self, mock_bank):
        user = User('Fariseo', '1234567', 'Serranos', '65612648', 'hola@adios.com')
        flight = Flight('abc', 4, 'Paris', 'Barcelona', 99.99)
        flight2 = Flight('def', 4, 'Barcelona', 'New York', 399.99)
        flight3 = Flight('ghi', 4, 'New York', 'Paris', 299.99)
        trip = Trip(user)
        trip.add_flight(flight)
        trip.add_flight(flight2)
        trip.add_flight(flight3)
        total_price = trip.get_total_price_with_iva()
        payment = PaymentData('Visa', 'Fariseo', '6456456454', '654', total_price)
        mock_bank.do_payment.return_value = False
        res = mock_bank.do_payment(user, payment)
        confirmed = trip.confirm_payment(res)
        self.assertEqual('Payment has been denied.', confirmed)

    @mock.patch('src.Skyscanner')
    def test_given_a_confirmation_error_when_reserving_flights_report_a_message_error(self, mock_sky):
        user = User('Fariseo', '1234567', 'Serranos', '65612648', 'hola@adios.com')
        flight = Flight('abc', 4, 'Paris', 'Barcelona', 99.99)
        flight2 = Flight('def', 4, 'Barcelona', 'New York', 399.99)
        flight3 = Flight('ghi', 4, 'New York', 'Paris', 299.99)
        trip = Trip(user)
        trip.add_flight(flight)
        trip.add_flight(flight2)
        trip.add_flight(flight3)
        flights = trip.get_flights()
        mock_sky.confirm_reserve.return_value = False
        res = mock_sky.confirm_reserve(user, flights)
        confirmed = trip.confirm_flight_reservation(res)
        self.assertEqual('Your flight reservation has been denied.', confirmed)

    # ------------------------------------------------ Tests Version 3 ------------------------------------------------

    def test_price_add_car(self):
        user = User('Fariseo', '1234567', 'Serranos', '65612648', 'hola@adios.com')
        car = Car('1345FHZ', 'Ferrari', 'La Mina', 3, 1499.99)
        trip = Trip(user)
        trip.add_car(car)
        self.assertEqual(4499.97, trip.get_total_price_with_iva())

    def test_price_delete_car(self):
        user = User('Fariseo', '1234567', 'Serranos', '65612648', 'hola@adios.com')
        car = Car('1345FHZ', 'Ferrari', 'La Mina', 3, 1499.99)
        car2 = Car('5648PSD', 'Xaara Picasso', 'Pedralbes', 3, 19.99)
        trip = Trip(user)
        trip.add_car(car)
        trip.add_car(car2)
        trip.delete_car(car)
        self.assertAlmostEqual(59.97, trip.get_total_price_with_iva())

    def test_price_add_hotel(self):
        user = User('Fariseo', '1234567', 'Serranos', '65612648', 'hola@adios.com')
        hotel = Hotel('xyz', 'Hotel W', 2, 1, 3, 149.99)
        trip = Trip(user)
        trip.add_hotel(hotel)
        self.assertEqual(899.94, trip.get_total_price_with_iva())

    def test_price_delete_hotel(self):
        user = User('Fariseo', '1234567', 'Serranos', '65612648', 'hola@adios.com')
        hotel = Hotel('xyz', 'Hotel W', 2, 1, 3, 149.99)
        hotel2 = Hotel('jkl', 'Hostal Menchu', 2, 1, 1, 14.99)
        trip = Trip(user)
        trip.add_hotel(hotel)
        trip.add_hotel(hotel2)
        trip.delete_hotel(hotel)
        self.assertAlmostEqual(29.98, trip.get_total_price_with_iva())

    def test_given_a_car_list_when_its_reserved_then_returns_text_confirmation(self):
        user = User('Fariseo', '1234567', 'Serranos', '65612648', 'hola@adios.com')
        flight = Flight('abc', 2, 'Paris', 'Barcelona', 99.99)
        flight2 = Flight('def', 2, 'Barcelona', 'New York', 399.99)
        car = Car('1345FHZ', 'Ferrari', 'La Mina', 3, 1499.99)
        car2 = Car('5648PSD', 'Xaara Picasso', 'Central Park', 3, 19.99)
        trip = Trip(user)
        trip.add_flight(flight)
        trip.add_flight(flight2)
        trip.add_car(car)
        trip.add_car(car2)
        cars = trip.get_hotels()
        rent = Rentalcars()
        res = rent.confirm_reserve(user, cars)
        confirmed = trip.confirm_car_reservation(res)
        self.assertEqual('Your cars have been reserved successfully.', confirmed)

    @mock.patch('src.Rentalcars')
    def test_given_a_confirmation_error_when_reserving_cars_report_a_message_error(self, mock_rent):
        user = User('Fariseo', '1234567', 'Serranos', '65612648', 'hola@adios.com')
        flight = Flight('abc', 2, 'Paris', 'Barcelona', 99.99)
        flight2 = Flight('def', 2, 'Barcelona', 'New York', 399.99)
        car = Car('1345FHZ', 'Ferrari', 'La Mina', 3, 1499.99)
        car2 = Car('5648PSD', 'Xaara Picasso', 'Central Park', 3, 19.99)
        trip = Trip(user)
        trip.add_flight(flight)
        trip.add_flight(flight2)
        trip.add_car(car)
        trip.add_car(car2)
        cars = trip.get_cars()
        mock_rent.confirm_reserve.return_value = False
        res = mock_rent.confirm_reserve(user, cars)
        confirmed = trip.confirm_car_reservation(res)
        self.assertEqual('Your car reservation has been denied.', confirmed)

    def test_given_a_hotel_list_when_its_reserved_then_returns_text_confirmation(self):
        user = User('Fariseo', '1234567', 'Serranos', '65612648', 'hola@adios.com')
        flight = Flight('abc', 2, 'Paris', 'Barcelona', 99.99)
        flight2 = Flight('def', 2, 'Barcelona', 'New York', 399.99)
        hotel = Hotel('xyz', 'Hotel W', 2, 1, 3, 149.99)
        hotel2 = Hotel('jkl', 'Hostal Menchu', 2, 1, 1, 14.99)
        trip = Trip(user)
        trip.add_flight(flight)
        trip.add_flight(flight2)
        trip.add_hotel(hotel)
        trip.add_hotel(hotel2)
        hotels = trip.get_hotels()
        book = Booking()
        res = book.confirm_reserve(user, hotels)
        confirmed = trip.confirm_hotel_reservation(res)
        self.assertEqual('Your hotels have been reserved successfully.', confirmed)

    @mock.patch('src.Booking')
    def test_given_a_confirmation_error_when_reserving_hotels_report_a_message_error(self, mock_book):
        user = User('Fariseo', '1234567', 'Serranos', '65612648', 'hola@adios.com')
        flight = Flight('abc', 2, 'Paris', 'Barcelona', 99.99)
        flight2 = Flight('def', 2, 'Barcelona', 'New York', 399.99)
        hotel = Hotel('xyz', 'Hotel W', 2, 1, 3, 149.99)
        hotel2 = Hotel('jkl', 'Hostal Menchu', 2, 1, 1, 14.99)
        trip = Trip(user)
        trip.add_flight(flight)
        trip.add_flight(flight2)
        trip.add_hotel(hotel)
        trip.add_hotel(hotel2)
        hotels = trip.get_hotels()
        mock_book.confirm_reserve.return_value = False
        res = mock_book.confirm_reserve(user, hotels)
        confirmed = trip.confirm_hotel_reservation(res)
        self.assertEqual('Your hotel reservation has been denied.', confirmed)

# ------------------------------------------------ Tests Version 4 ------------------------------------------------

    @mock.patch('src.Bank')
    def test_given_an_error_when_paying_then_retry_payment(self, mock_bank):
        user = User('Fariseo', '1234567', 'Serranos', '65612648', 'hola@adios.com')
        flight = Flight('abc', 4, 'Paris', 'Barcelona', 99.99)
        flight2 = Flight('def', 4, 'Barcelona', 'New York', 399.99)
        flight3 = Flight('ghi', 4, 'New York', 'Paris', 299.99)
        trip = Trip(user)
        trip.add_flight(flight)
        trip.add_flight(flight2)
        trip.add_flight(flight3)
        total_price = trip.get_total_price_with_iva()
        payment = PaymentData('Visa', 'Fariseo', '6456456454', '654', total_price)
        mock_bank.do_payment.return_value = False
        res = mock_bank.do_payment(user, payment)
        if not res:
            mock_bank.do_payment.return_value = True
            res = mock_bank.do_payment(user, payment)
        self.assertTrue(res)

    @mock.patch('src.Bank')
    def test_when_retrying_a_payment_show_confirmation_message(self, mock_bank):
        user = User('Fariseo', '1234567', 'Serranos', '65612648', 'hola@adios.com')
        flight = Flight('abc', 4, 'Paris', 'Barcelona', 99.99)
        flight2 = Flight('def', 4, 'Barcelona', 'New York', 399.99)
        flight3 = Flight('ghi', 4, 'New York', 'Paris', 299.99)
        trip = Trip(user)
        trip.add_flight(flight)
        trip.add_flight(flight2)
        trip.add_flight(flight3)
        total_price = trip.get_total_price_with_iva()
        payment = PaymentData('Visa', 'Fariseo', '6456456454', '654', total_price)
        mock_bank.do_payment.return_value = False
        res = mock_bank.do_payment(user, payment)
        confirm = trip.confirm_payment(res)
        if not res:
            mock_bank.do_payment.return_value = True
            res = mock_bank.do_payment(user, payment)
            confirm = trip.confirm_payment(res)
        self.assertEqual('Payment has been done successfully.', confirm)


if __name__ == '__main__':
    unittest.main()
