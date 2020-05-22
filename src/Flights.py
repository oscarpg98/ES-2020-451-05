from src.Flight import Flight


class Flights:

    def __init__(self):
        self.flight_list = []
        self.destination_list = []
        self.flights_price = 0.0

    def get_destination_list(self):
        return self.destination_list

    def get_flights_price(self):
        return self.flights_price

    @staticmethod
    def get_id(flight: Flight):
        return flight.get_flight_id()

    def get_id_list(self):
        ids = []
        for i in self.flight_list:
            ids.append(i.get_flight_id())
        return ids

    def add_flight(self, flight: Flight):
        self.flight_list.append(flight)
        self.destination_list.append(flight.get_destination())
        self.flights_price += (flight.get_price()*float(flight.get_passenger_num()))

    def delete_flight(self, flight: Flight):
        self.flights_price -= (flight.get_price()*float(flight.get_passenger_num()))
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
