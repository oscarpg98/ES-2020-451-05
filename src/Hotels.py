from src.Hotel import Hotel


class Hotels:

    def __init__(self):
        self.hotel_list = []
        self.hotels_price = 0.0

    def get_hotels_price(self):
        return self.hotels_price

    def add_hotel(self, hotel: Hotel):
        self.hotel_list.append(hotel)
        self.hotels_price += (hotel.get_price() * float(hotel.get_hosts() * hotel.get_days()))

    def delete_hotel(self, hotel: Hotel):
        self.hotels_price -= (hotel.get_price() * float(hotel.get_hosts() * hotel.get_days()))
        self.hotel_list.remove(hotel)
