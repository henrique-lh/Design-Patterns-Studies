
from abc import ABCMeta, abstractmethod
from dataclasses import dataclass
from decimal import Decimal


@dataclass
class CarProduct:

    price: Decimal = None
    dscMotor: str = None
    year: int = None
    model: str = None
    automaker: str = None


@dataclass
class BuilderCar(metaclass=ABCMeta):

    _car: CarProduct = CarProduct()

    @abstractmethod
    def build_price(self) -> None:
        pass

    @abstractmethod
    def build_dsc_motor(self) -> None:
        pass

    @abstractmethod
    def build_year(self) -> None:
        pass

    @abstractmethod
    def build_model(self) -> None:
        pass

    def build_automaker(self) -> None:
        pass

    @property
    def car(self) -> CarProduct:
        return self._car


@dataclass
class Fiat(BuilderCar):

    def build_price(self) -> None:
        self._car.price = Decimal("25000.00")

    def build_dsc_motor(self) -> None:
        self._car.dscMotor = "Fire Flex 1.0"

    def build_year(self) -> None:
        self._car.year = 2011

    def build_model(self) -> None:
        self._car.model = "Palio"

    def build_automaker(self) -> None:
        self._car.automaker = "Fiat"


@dataclass
class Volks(BuilderCar):

    def build_price(self) -> None:
        self._car.price = Decimal("15000.00")

    def build_dsc_motor(self) -> None:
        self._car.dscMotor = "Fire Flex 1.0"

    def build_year(self) -> None:
        self._car.year = 2011

    def build_model(self) -> None:
        self._car.model = "GOL"

    def build_automaker(self) -> None:
        self._car.automaker = "Volks"


class Dealership:

    _automaker: BuilderCar = None

    def __init__(self, build_car: BuilderCar) -> None:
        Dealership._automaker = build_car

    def build_car(self) -> None:
        self._automaker.build_price()
        self._automaker.build_dsc_motor()
        self._automaker.build_year()
        self._automaker.build_model()
        self._automaker.build_automaker()

    @property
    def get_car(self) -> BuilderCar:
        return self._automaker.car


if __name__ == '__main__':

    dealership = Dealership(Fiat())
    dealership.build_car()

    car = dealership.get_car
    print(car)

    dealership = Dealership(Volks())
    dealership.build_car()
    print(car)
