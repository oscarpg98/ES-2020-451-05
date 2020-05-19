class Hotels:

    def __init__(self, hotel_id: str, name: str, hosts: int, rooms: int, days: int, price: float):
        self.hotel_id = hotel_id
        self.name = name
        self.hosts = hosts
        self.rooms = rooms
        self.days = days
        self.price = price

    def get_hotel_id(self):
        return self.hotel_id

    def get_name(self):
        return self.name

    def get_hosts(self):
        return self.hosts

    def get_rooms(self):
        return self.rooms

    def get_days(self):
        return self.days

    def get_price(self):
        return self.price
