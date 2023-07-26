class Car:
    def assign_driver(self, driver_name):
        print(f"{driver_name} is driving the car")

class Motorcycle:
    def assign_rider(self, rider_name):
        print(f"{rider_name} is riding the motorcycle")

class MotorcycleAdapter:

    def __init__(self, motorcycle):
        self.motorcycle = motorcycle

    def assign_driver(self, name):
        self.motorcycle.assign_rider(name)

if __name__ == '__main__':
    car = Car()
    bike = Motorcycle()
    bike_adapter = MotorcycleAdapter(bike)
    bike_adapter.assign_driver("Robert")
