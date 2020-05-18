class Flights:

    def __init__(self, codi_vol: str = None, num_pasajeros: int = None, origen: str = None, destinacion: str = None):
        self.id_vuelo = codi_vol
        self.num_pasajeros = num_pasajeros
        self.origen = origen
        self.destinacion = destinacion
        pass

    def get_num_pass(self):
        return self.num_pasajeros
        pass

    def get_codi_vol(self):
        return self.id_vuelo
        pass

    def get_destinacion(self):
        return self.destinacion
        pass
