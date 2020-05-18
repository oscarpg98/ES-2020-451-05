class Cars:

    def __init__(self, car_id: str, brand: str, picking_place: str, duration: int):
        self.car_id = car_id
        self.brand = brand
        self.picking_place = picking_place
        self.duration = duration

    def get_car_id(self):
        return self.car_id

    def get_brand(self):
        return self.brand

    def get_picking_place(self):
        return self.picking_place

    def duration(self):
        return self.duration
