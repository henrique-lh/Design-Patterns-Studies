class MotorCycle:

    def __init__(self) -> None:
        self.name = "MotorCycle"

    def two_wheeler(self) -> str:
        return "TwoWheeler"


class Truck:

    def __init__(self) -> None:
        self.name = "Truck"

    def eight_wheeler(self) -> str:
        return "EightWheeler"


class Car:

    def __init__(self) -> None:
        self.name = "Car"

    def four_wheeler(self) -> str:
        return "FourWheeler"


class Adapter:

    def __init__(self, obj, **adapted_methods) -> None:
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __getattr__(self, attr):
        return getattr(self.obj, attr)

    def original_dict(self):
        return self.obj.__dict__

""" main method """
def main() -> None:
    """list to store objects"""
    objects = []

    motorCycle = MotorCycle()
    objects.append(Adapter(motorCycle, wheels = motorCycle.two_wheeler))

    truck = Truck()
    objects.append(Adapter(truck, wheels = truck.eight_wheeler))

    car = Car()
    objects.append(Adapter(car, wheels = car.four_wheeler))

    for obj in objects:
        print("A {0} is a {1} vehicle".format(obj.name, obj.wheels()))

if __name__ == "__main__":
    main()