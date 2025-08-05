# Smartphone class with inheritance and encapsulation

class Smartphone:
    def __init__(self, brand, model, battery):
        self.brand = brand
        self.model = model
        self.__battery = battery

    def make_call(self, number):
        print(f"{self.brand} {self.model} is calling {number}...")

    def battery_status(self):
        print(f"Battery level: {self.__battery}%")

    def charge(self, amount):
        self.__battery = min(self.__battery + amount, 100)
        print(f"Charging... Battery is now {self.__battery}%")

# Inherited class
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, battery, gpu):
        super().__init__(brand, model, battery)
        self.gpu = gpu

    def play_game(self, game):
        print(f"Playing {game} on {self.brand} {self.model} with {self.gpu} GPU!")

# Create objects
phone1 = Smartphone("Samsung", "Galaxy S22", 75)
phone1.make_call("0712345678")
phone1.battery_status()
phone1.charge(15)

print()

gaming_phone = GamingSmartphone("Asus", "ROG Phone 6", 50, "Adreno 730")
gaming_phone.play_game("PUBG Mobile")
gaming_phone.battery_status()
