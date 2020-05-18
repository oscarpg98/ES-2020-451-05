class User:

    def __init__(self, name: str, dni: str, address: str, phone: str, email: str):
        self.name = name
        self.dni = dni
        self.address = address
        self.phone = phone
        self.email = email

    def get_name(self):
        return self.name

    def get_dni(self):
        return self.dni

    def get_address(self):
        return self.address

    def get_phone(self):
        return self.phone

    def get_email(self):
        return self.email
