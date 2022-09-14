from abc import ABC, abstractmethod
from typing import List


class Item:
    def __init__(self, nome: str, valor: int) -> None:
        self.nome = nome
        self.valor = valor

    def __repr__(self) -> str:
        return f"Item(nome={self.nome}, valor={self.valor})"


class Carrinho:
    def __init__(self) -> None:
        self.itens: List[Item] = []

    def adicionar_item(self, item: Item) -> None:
        self.itens.append(item)

    @property
    def valor(self) -> int:
        return sum(map(lambda item: item.valor, self.itens))


class Promocao(ABC):

    @abstractmethod
    def calcular(self, valor):
        pass


class Promocao5NoCarrinho(Promocao):
    def __init__(self, next=None) -> None:
        self.next = next

    def calcular(self, carrinho: Carrinho) -> float:
        if len(carrinho.itens) >= 5:
            return carrinho.valor - (carrinho.valor * 0.1)
        return self.next.calcular(carrinho)


class PromocaoMaisDeMil(Promocao):
    def __init__(self, next=None) -> None:
        self.next = next

    def calcular(self, carrinho: Carrinho) -> float:
        if carrinho.valor >= 1_000:
            return carrinho.valor - (carrinho.valor * 0.2)
        return self.next.calcular(carrinho)

class SemPromocao(Promocao):

    def calcular(self, carrinho: Carrinho) -> float:
        return carrinho.valor


class CalculadoraDePromocoes:
    def calcular(self, valor: int) -> float:
        p1 = PromocaoMaisDeMil()
        p2 = Promocao5NoCarrinho()
        p3 = SemPromocao()

        p1.next = p2
        p2.next = p3

        return p1.calcular(valor)


if __name__ == "__main__":

    # Primeira promoção
    carrinho = Carrinho()

    carrinho.adicionar_item(Item("Fritas", 8))
    carrinho.adicionar_item(Item("Fritas", 8))
    carrinho.adicionar_item(Item("Fritas", 8))
    carrinho.adicionar_item(Item("Fritas", 8))
    carrinho.adicionar_item(Item("Fritas", 8))

    cp = CalculadoraDePromocoes()
    print(f"Valor sem promoção: {carrinho.valor}")
    print(f"Valor com promoção: {cp.calcular(carrinho)}")
    print("\n")

    # Segunda promoção
    carrinho = Carrinho()

    carrinho.adicionar_item(Item("Fritas", 8))
    carrinho.adicionar_item(Item("Fritas", 8))
    carrinho.adicionar_item(Item("Fritas", 8))
    carrinho.adicionar_item(Item("Fritas", 8))
    carrinho.adicionar_item(Item("Fritas", 8))
    carrinho.adicionar_item(Item("Camera", 1000))

    cp = CalculadoraDePromocoes()
    print(f"Valor sem promoção: {carrinho.valor}")
    print(f"Valor com promoção: {cp.calcular(carrinho)}")
    print("\n")

    # Sem promoção
    carrinho = Carrinho()

    carrinho.adicionar_item(Item("Graviola", 1))

    cp = CalculadoraDePromocoes()
    print(f"Valor sem promoção: {carrinho.valor}")
    print(f"Valor com promoção: {cp.calcular(carrinho)}")