#from electric_car import Car, ElectricCar
import electric_car

my_beetle = electric_car.Car('volkswagen', 'beetle', 2016)
my_tesla = electric_car.ElectricCar('tesla', 'model s', 2016)

print(my_beetle.get_descriptive_name())
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
