import exceptions
from car import Car
from plane import Plane

car = Car(100, 0, 0.4)
try:
    car.start()
except exceptions.LowFuelError:
    print('LowFuelError')

plane = Plane(100, 0, 0.4, 10)
try:
    plane.start()
except exceptions.LowFuelError:
    print('LowFuelError')

try:
    plane.load_cargo(100)
except exceptions.CargoOverload:
    print('CargoOverload')

try:
    car.move(100)
except exceptions.NotEnoughFuel:
    print('NotEnoughFuel')

plane.remove_all_cargo()