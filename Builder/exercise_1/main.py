from __future__ import annotations
from abc import ABCMeta, abstractmethod


class Builder(metaclass=ABCMeta):

    @property
    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def produce_company(self) -> None:
        pass

    @abstractmethod
    def reset(self) -> None:
        pass


class ConcreteBuild(Builder):

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = Empresa()

    @property
    def product(self) -> Empresa:
        p = self._product
        self.reset()
        return p

    def produce_company(self) -> None:
        nf = input()
        nome = input()
        identidade = input()
        self._product.company_name = nf
        self._product.prop = Pessoa(nome, identidade)


class Empresa:
    
    def __init__(self) -> None:
        self._company_name: str = None
        self._prop: Pessoa = None

    @property
    def company_name(self) -> str:
        return self._company_name

    @company_name.setter
    def company_name(self, company_name: str) -> None:
        self._company_name = company_name

    @property
    def prop(self) -> str:
        return self._prop

    @prop.setter
    def prop(self, prop: Pessoa) -> None:
        self._prop = prop

    def __repr__(self) -> str:
        return f"""{'-' * 50}
- Nome da empresa: {self.company_name}
- Proprietário: {self.prop}
"""

class Pessoa:

    def __init__(self, nome: str, identidade: str) -> None:
        self._nome = nome
        self._identidade = identidade

    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, nome: str) -> None:
        self._nome = nome

    @property
    def identidade(self) -> str:
        return self._identidade

    @identidade.setter
    def identidade(self, identidade: str) -> None:
        self._identidade = identidade

    def __repr__(self) -> str:
        return f"""
    * Nome: {self.nome}
    * Identidade: {self.identidade}"""


class Director:

    def __init__(self) -> None:
        self._builder: Builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder

    def build_new_company(self) -> None:
        self._builder.produce_company()


def main() -> None:

    director = Director()
    builder = ConcreteBuild()
    director.builder = builder

    for i in range(3):
        director.build_new_company()
        print(builder.product)

if __name__ == "__main__":
    main()
