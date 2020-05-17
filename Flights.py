class Flights:

    def __init__(self,codiVol:str, numPasajeros:int, Origen:str, Destinaciones:str):
        self.id_vuelo=codiVol
        self.num_pasajeros = numPasajeros
        self.origen = Origen
        self.destinaciones = Destinaciones
        pass
    
    def getNumPass(self):
        return self.num_pasajeros
        pass
    
    def getCodiVol(self):
        return self.id_vuelo
        pass
