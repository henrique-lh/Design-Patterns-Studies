from abc import ABC, abstractmethod


class Alvo(ABC):

    @abstractmethod
    def operacao(self):
        pass

class ClasseExistente:

    def metodoUtilUm(self, text: str) -> None:
        print(text)

    def metodoUtilDois(self, text: str) -> str:
        return text.upper()

class Adaptador(ClasseExistente, Alvo):

    def operacao(self) -> None:
        text = self.metodoUtilDois("Operação Realizada")
        self.metodoUtilUm(text)


def main() -> None:
    alvo = Adaptador()
    alvo.operacao()

if __name__ == "__main__":
    main()