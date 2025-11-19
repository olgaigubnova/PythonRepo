from mailing import Mailing
from address import Address

to_address = Address("123456", "Moscow", "Lenina", "10", "5")
from_address = Address("654321", "Saint Petersburg", "Kirova", "20", "10")  
track = "TRACK123456789"
cost = 250

mailing = Mailing(to_address, from_address, cost, track)
print(mailing)
