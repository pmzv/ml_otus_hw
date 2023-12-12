from vehicle import Vehicle
import exceptions


class Plane(Vehicle):

    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        super().__init__(weight, fuel, fuel_consumption)
        self.cargo = 0
        self.max_cargo = max_cargo

    def load_cargo(self, number):
        if self.cargo + number > self.max_cargo:
            raise exceptions.CargoOverload
        self.cargo += number

    def remove_all_cargo(self):
        cur_cargo = self.cargo
        self.cargo = 0
        return cur_cargo
