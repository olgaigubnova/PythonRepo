from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 13", "+79012345670"),
    Smartphone("Samsung", "Galaxy S21", "+79876543210"),  
    Smartphone("Google", "Pixel 6", "+71122334455")
]
for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. {smartphone.phone_number}") 
