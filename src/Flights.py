class Flights:

    def __init__(self, flight_id: str, passenger_num: int, origin: str, destination: str):
        self.flight_id = flight_id
        self.passenger_num = passenger_num
        self.origin = origin
        self.destination = destination

    def get_passenger_num(self):
        return self.passenger_num

    def get_flight_id(self):
        return self.flight_id

    def get_destination(self):
        return self.destination

    def destination_is_empty(self) -> bool:
        n = len(self.destination)
        if n == 0:
            return True
        return False
