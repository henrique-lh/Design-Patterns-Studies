from typing import Callable, List


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


def promocao_cinco_no_carrinho(carrinho: Carrinho) -> float:
    if len(carrinho.itens) >= 5:
        return carrinho.valor - (carrinho.valor * 0.1)

def promocao_mais_de_mil(carrinho: Carrinho) -> float:
    if carrinho.valor >= 1_000:
        return carrinho.valor - (carrinho.valor * 0.2)


class CalculadoraDePromocoes:

    def __init__(self, *promos: Callable) -> None:
        self.promos = promos

    def __call__(self, carrinho: Carrinho) -> float:
        for promo in self.promos:
            if (resultado := promo(carrinho)):
                return resultado

        return self.callback(carrinho)

    def callback(self, carrinho: Carrinho) -> float:
        return carrinho.valor


if __name__ == "__main__":

    carrinho = Carrinho()

    cp = CalculadoraDePromocoes(
        promocao_cinco_no_carrinho,
        promocao_mais_de_mil,
    )

    carrinho.adicionar_item(Item("Camera", 1000))
    carrinho.adicionar_item(Item("Graviola", 1))

    print(f"Valor sem promocação: {carrinho.valor}")
    print(f"Valor com promoção: {cp(carrinho)}")