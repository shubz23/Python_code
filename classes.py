

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_description(self):
        return f"{self.year} {self.make} {self.model}"

    def read_odometer(self):
        return f"This car has {self.odometer_reading} miles on it."

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

# Creating an instance of the Car class
my_car = Car("Toyota", "Corolla", 2019)

# Accessing attributes and calling methods of the Car instance
print(f"My car: {my_car.get_description()}")
print(my_car.read_odometer())

# Modifying an attribute using a method
my_car.update_odometer(10000)
print(my_car.read_odometer())

# Incrementing an attribute value using a method
my_car.increment_odometer(100)
print(my_car.read_odometer())