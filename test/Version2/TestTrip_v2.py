from src.Trip import Trip
from src.Flight import Flight
from src.User import User
from src.PaymentData import PaymentData
from src.Bank import Bank
from unittest import mock
from src.Skyscanner import Skyscanner
import unittest


class TestTripV2(unittest.TestCase):

    def test_payment_method(self):
        user = User('Fariseo', '1234567', 'Serranos', '65612648', 'hola@adios.com')
        flight = Flight('abc', 4, 'Paris', 'Barcelona', 99.99)
        flight2 = Flight('def', 4, 'Barcelona', 'New York', 399.99)
        trip = Trip(user)
        trip.add_flight(flight)
        trip.add_flight(flight2)
        total_price = trip.get_total_price()
        payment = PaymentData('Visa', 'Fariseo', '6456456454', '654', total_price)
        bank = Bank()
        trip.do_payment(user, payment, bank)
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
        total_price = trip.get_total_price()
        payment = PaymentData('Visa', 'Fariseo', '6456456454', '654', total_price)
        mock_bank.do_payment(user, payment).return_value = False
        res = trip.do_payment(user, payment, mock_bank)
        self.assertEqual('Payment has been denied.', res)

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
        mock_sky.return_value.confirm_reserve(user, flights).return_value = False
        self.assertEqual('Your flight reservation has been denied.', trip.confirm_flight_reservation(user))


if __name__ == '__main__':
    unittest.main()
