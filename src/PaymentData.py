class PaymentData:

    def __init__(self):
        self.tipo = str(input())
        self.titular = str(input())
        self.num_tarjeta = int(input())
        self.cvv = int(input())
        self.importe = int(input())
        pass
