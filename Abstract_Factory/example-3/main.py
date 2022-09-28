from __future__ import annotations
from abc import ABCMeta, abstractmethod

class CarFactory(metaclass=ABCMeta):

    @abstractmethod
    def create_sedan_car(self) -> SedanCar:
        pass

    @abstractmethod
    def create_popular_car(self) -> PopularCar:
        pass


class FiatFactory(CarFactory):

    def create_sedan_car(self) -> SedanCar:
        return Siena()

    def create_popular_car(self) -> PopularCar:
        return Palio()


class FordFactory(CarFactory):

    def create_sedan_car(self) -> SedanCar:
        return FiestaSedan()

    def create_popular_car(self) -> PopularCar:
        return Fiesta()


class PopularCar(metaclass=ABCMeta):

    def info(self) -> None:
        pass


class SedanCar(metaclass=ABCMeta):

    def info(self) -> None:
        pass


class Palio(PopularCar):

    def info(self) -> None:
        print("Model: Palio")
        print("Factory: Fiat")
        print('Category: Popular')


class Siena(SedanCar):

    def info(self) -> None:
        print("Model: Siena")
        print("Factory: Fiat")
        print('Category: Sedan')


class FiestaSedan(SedanCar):

    def info(self) -> None:
        print("Model: Fiesta Sedan")
        print("Factory: Ford")
        print('Category: Sedan')


class Fiesta(PopularCar):

    def info(self) -> None:
        print("Model: Fiesta")
        print("Factory: Ford")
        print('Category: Popular')


def main() -> None:

    print('Fiat factory....')
    factory = FiatFactory()
    sedan = factory.create_sedan_car()
    popular = factory.create_popular_car()
    sedan.info()
    print()
    popular.info()

    print('\n--------------------\nFiat factory....')
    factory = FordFactory()
    sedan = factory.create_sedan_car()
    popular = factory.create_popular_car()
    sedan.info()
    print()
    popular.info()

if __name__ == "__main__":
    main()