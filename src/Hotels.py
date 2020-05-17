class Hotels:

    def __init__(self, codigo_hotel: str, nombre: str, n_huespedes: int, n_habitaciones: int, d_estancia: int):
        self.codigo_hotel = codigo_hotel
        self.nombre = nombre
        self.n_huespedes = n_huespedes
        self.n_habitaciones = n_habitaciones
        self.d_estancia = d_estancia
        pass

    def get_codigo_hotel(self):
        return self.codigo_hotel

    def get_nombre(self):
        return self.nombre

    def get_n_huespedes(self):
        return self.n_huespedes

    def get_n_habitaciones(self):
        return self.n_habitaciones

    def get_d_estancia(self):
        return self.d_estancia
