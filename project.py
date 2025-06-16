class BMW:
    def fuel_type(self):
        return "Petrol"
    def max_speed(self):
        return "250 km/h"
class Ferrari:
    def fuel_type(self):
        return "Hybrid"
    def max_speed(self):
        return "340 km/h"
def vehicle_info(vehicle):
    print("Fuel Type: {vehicle.fuel_type()}")
    print("Max Speed: {vehicle.max_speed()}")
bmw_car = BMW()
ferrari_car = Ferrari()
print("BMW Info:")
vehicle_info(bmw_car)
print("\nFerrari Info:")
vehicle_info(ferrari_car)