from src.Car import Car


class Cars:

    def __init__(self):
        self.car_list = []
        self.cars_price = 0.0

    def get_cars_price(self):
        return self.cars_price

    def add_car(self, car: Car):
        self.car_list.append(car)
        self.cars_price += (car.get_price()*float(car.get_duration()))

    def delete_car(self, car: Car):
        self.cars_price -= (car.get_price() * float(car.get_duration()))
        self.car_list.remove(car)
