from abc import ABC, abstractclassmethod

class EuropeanSocketInterface(ABC):

    @abstractclassmethod
    def voltage(self): 
        pass

    @abstractclassmethod
    def live(self):
        pass

    @abstractclassmethod
    def neutral(self):
        pass

    @abstractclassmethod
    def earth(self):
        pass


class Socket(EuropeanSocketInterface):

    @property
    def voltage(self) -> int:
        return 230

    @property
    def live(self) -> int:
        return 1

    @property
    def neutral(self) -> int:
        return -1

    @property
    def earth(self) -> int:
        return 0


class USASocketInerface(ABC):

    @abstractclassmethod
    def voltage(self):
        pass

    @abstractclassmethod
    def live(self):
        pass

    @abstractclassmethod
    def neutral(self):
        pass


class Adapter(USASocketInerface):

    __socket = None

    def __init__(self, socket) -> None:
        self.__socket = socket

    @property
    def voltage(self) -> int:
        return 110

    def live(self):
        return self.__socket.live

    def neutral(self):
        return self.__socket.neutral


class EletricKettle:

    __power = None

    def __init__(self, power) -> None:
        self.__power = power

    def boil(self):
        if self.__power.voltage > 110:
            print("Kettle on fire!")
        elif self.__power.live() == 1 and self.__power.neutral() == -1:
            print("Coffee time!")
        else:
            print("No power.")


def main() -> None:
    socket = Socket()
    adapter = Adapter(socket)
    kettle = EletricKettle(adapter)

    kettle.boil()

if __name__ == "__main__":
    main()