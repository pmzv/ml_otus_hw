from abc import ABC
import exceptions


class Vehicle(ABC):

    def __init__(self, weight, fuel, fuel_consumption):
        self.started = None
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if self.fuel > 0:
            self.started = True
        else:
            raise exceptions.LowFuelError

    def move(self, distance=0):
        if self.fuel / self.fuel_consumption > distance:
            self.fuel = self.fuel - distance * self.fuel_consumption
        else:
            raise exceptions.NotEnoughFuel()


class Engine:

    def __init__(self):
        self.volume = 0
        self.pistons = 0
