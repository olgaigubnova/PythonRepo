from address import Address

class Mailing:
    def __init__(self, to_address, from_address, cost, track):
        self.to_address = to_address 
        self.from_address = from_address
        self.cost = cost
        self.track = track

    def __str__(self):

             return (f"Отправление {self.track} из {self.from_address.zip_code}, "
                f"{self.from_address.city}, {self.from_address.street}, "
                f"{self.from_address.house_number} - {self.from_address.apartment_number} "
                f"в {self.to_address.zip_code}, {self.to_address.city}, {self.to_address.street}, " 
                f"{self.to_address.house_number} - {self.to_address.apartment_number}. "
                f"Стоимость: {self.cost} рублей.")
    
    

          