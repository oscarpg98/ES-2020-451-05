from src.Trip import Trip
from src.Flights import Flights
from src.User import User
from src.PaymentData import PaymentData
from src.Bank import Bank
from unittest import mock
import unittest


class TestTripV2(unittest.TestCase):

    def test_payment_method(self):
        user = User('Fariseo', '1234567', 'Serranos', '65612648', 'hola@adios.com')
        flight = Flights('abc', 4, 'Paris', 'Barcelona', 99.99)
        trip = Trip(user)
        trip.add_flight(flight)
        total_price = trip.get_total_price()
        payment = PaymentData('Visa', 'Fariseo', '6456456454', '654', total_price)
        done, _ = payment.do_payment(user)
        if done:
            self.assertEqual('Visa', payment.get_card_type())

    @mock.patch('src.Bank')
    def test_payment_denied(self, mock_payment):
        user = User('Fariseo', '1234567', 'Serranos', '65612648', 'hola@adios.com')
        flight = Flights('abc', 4, 'Paris', 'Barcelona', 99.99)
        flight2 = Flights('def', 4, 'Barcelona', 'New York', 399.99)
        flight3 = Flights('ghi', 4, 'New York', 'Paris', 299.99)
        trip = Trip(user)
        trip.add_flight(flight)
        trip.add_flight(flight2)
        trip.add_flight(flight3)
        total_price = trip.get_total_price()
        payment = PaymentData('Visa', 'Fariseo', '6456456454', '654', total_price)
        #No sabemos falsear la respuesta de la función do_payment del Bank.
        mock_payment.return_value = False
        bank = Bank()
        self.assertFalse(bank.do_payment(user, payment))


if __name__ == '__main__':
    unittest.main()
