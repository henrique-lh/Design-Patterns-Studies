"""https://brizeno.wordpress.com/2011/10/26/mao-na-massa-mediator/"""

from __future__ import annotations
from abc import ABCMeta, abstractmethod
from typing import List

class Colleague(metaclass=ABCMeta):

    def __init__(self, m: Mediator) -> None:
        self._mediator = m

    def send_message(self, message: str) -> None:
        self._mediator.send(message, self)

    @abstractmethod
    def receive(self, message: str) -> None:
        pass


class IOSColleague(Colleague):

    def __init__(self, m: Mediator) -> None:
        super().__init__(m)

    
    def receive(self, message: str) -> None:
        print("iOs received:", message)


class AndroidColleague(Colleague):

    def __init__(self, m: Mediator) -> None:
        super().__init__(m)

    
    def receive(self, message: str) -> None:
        print("Android received:", message)


class Symbian(Colleague):

    def __init__(self, m: Mediator) -> None:
        super().__init__(m)

    def receive(self, message: str) -> None:
        print("Symbian received:", message)


class Mediator(metaclass=ABCMeta):

    @abstractmethod
    def send(self, message: str, colleague: Colleague) -> None:
        pass


class MediatorMessage(Mediator):

    def __init__(self) -> None:
        self._contacts: List[Colleague] = []

    def add_colleague(self, new_colleague: Colleague) -> None:
        self._contacts.append(new_colleague)

    def send(self, message: str, colleague: Colleague) -> None:
        for contact in self._contacts:
            if contact != colleague:
                self._define_protocoll(contact)
                contact.receive(message=message)

    def _define_protocoll(self, contact: Colleague) -> None:
        if isinstance(contact, IOSColleague):
            print("iOs protocoll")
        elif isinstance(contact, AndroidColleague):
            print("Android protocoll")
        elif isinstance(contact, Symbian):
            print("Symbian protocoll")

def lines() -> None:
    print("-" * 40)

def main() -> None:

    mediator = MediatorMessage()

    android = AndroidColleague(m=mediator)
    ios = IOSColleague(m=mediator)
    symbian = Symbian(m=mediator)

    mediator.add_colleague(android)
    mediator.add_colleague(ios)
    mediator.add_colleague(symbian)

    symbian.send_message("Hello, I'm a Symbian!")
    lines()

    android.send_message("Hello, I'm an Android!")
    lines()

    ios.send_message("Hello everyone, I'm an iOs!")

if __name__ == "__main__":
    main()