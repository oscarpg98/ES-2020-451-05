class PaymentData:

    def __init__(self, card_type: str, owner: str, card_number: str, cvv: int, price: float):
        self.card_type = card_type
        self.owner = owner
        self.card_number = card_number
        self.cvv = cvv
        self.price = price
        pass

    def get_card_type(self):
        return self.card_type

    def get_owner(self):
        return self.owner

    def get_card_number(self):
        return self.card_number

    def get_cvv(self):
        return self.cvv

    def get_price(self):
        return self.price
