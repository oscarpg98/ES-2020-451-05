class Flight:

    def __init__(self, flight_id: str, passenger_num: int, origin: str, destination: str, price: float):
        self.flight_id = flight_id
        self.passenger_num = passenger_num
        self.origin = origin
        self.destination = destination
        self.price = price

    def get_passenger_num(self):
        return self.passenger_num

    def get_flight_id(self):
        return self.flight_id

    def get_destination(self):
        return self.destination

    def get_price(self):
        return self.price
