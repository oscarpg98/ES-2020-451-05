class Car:

    def __init__(self, car_id: str, brand: str, picking_place: str, duration: int, price: float):
        self.car_id = car_id
        self.brand = brand
        self.picking_place = picking_place
        self.duration = duration
        self.price = price

    def get_car_id(self):
        return self.car_id

    def get_brand(self):
        return self.brand

    def get_picking_place(self):
        return self.picking_place

    def get_duration(self):
        return self.duration

    def get_price(self):
        return self.price
