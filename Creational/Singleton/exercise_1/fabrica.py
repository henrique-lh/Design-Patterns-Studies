from __future__ import annotations
from typing import Any, List

class _Singleton(type):

    _instances = {}
    num_of_calls = 0

    def __call__(cls, *args: Any, **kwds: Any) -> Any:
        _Singleton.num_of_calls += 1
        if cls not in cls._instances:
            cls._instances[cls] = super(_Singleton, cls).__call__(*args, **kwds)
        return cls._instances[cls]

    @classmethod
    def get_num_of_calls(cls) -> int:
        return _Singleton.num_of_calls


class Highlander(metaclass=_Singleton):
    pass

class Fabrica:

    num_of_calls = 0

    def __init__(self, number: int) -> None:
        Fabrica.num_of_calls += 1
        self._number = number
        self._box: List[Highlander] = []
        self.instanciate_highlander_objects()

    def instanciate_highlander_objects(self) -> None:
        for n in range(self._number):
            new_object = Highlander()
            self._box.append(new_object)

    @classmethod
    def total_instantiated_highlander_objects(cls) -> None:
        print(f"Total de vezes que a classe highlander foi instanciada: {Highlander.get_num_of_calls()}")
        print("-" * 50, "\n")

    @classmethod
    def number_of_factories(cls) -> int:
        return Fabrica.num_of_calls

def main() -> None:
    n: int

    while (n := input("Digite um número [Digite -1 para sair]: ")) != "-1":
        f = Fabrica(number=int(n))

    Fabrica.total_instantiated_highlander_objects()
    print(f"Quantidade de fábricas: {Fabrica.number_of_factories()}")

if __name__ == "__main__":
    main()