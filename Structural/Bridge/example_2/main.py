"""https://brizeno.wordpress.com/category/padroes-de-projeto/bridge/"""

from abc import ABCMeta, abstractmethod

class ImplementedWindow(metaclass=ABCMeta):

    @abstractmethod
    def draw_window(self, title: str) -> None:
        pass

    @abstractmethod
    def draw_button(self, title: str) -> None:
        pass


class Windows(ImplementedWindow):

    def draw_window(self, title: str) -> None:
        print(title, "- Janela Windows")

    def draw_button(self, title: str) -> None:
        print(title, "- Botão Windows")


class Linux(ImplementedWindow):

    def draw_window(self, title: str) -> None:
        print(title, "- Janela Linux")

    def draw_button(self, title: str) -> None:
        print(title, "- Botão Linux")


class MAC(ImplementedWindow):

    def draw_window(self, title: str) -> None:
        print(title, "- Janela MAC")

    def draw_button(self, title: str) -> None:
        print(title, "- Botão MAC")


class AbstractWindow(metaclass=ABCMeta):

    def __init__(self, j: ImplementedWindow) -> None:
        self._window = j

    def draw_window(self, title: str) -> None:
        self._window.draw_window(title)

    def draw_button(self, title: str) -> None:
        self._window.draw_button(title)

    @abstractmethod
    def draw(self) -> None:
        pass


class DialogueWindow(AbstractWindow):

    def __init__(self, j: ImplementedWindow) -> None:
        super().__init__(j)

    def draw(self) -> None:
        self.draw_window("Janela de Diálogo")
        self.draw_button("Botão Sim")
        self.draw_button("Botão Não")
        self.draw_button("Botão Cancelar")


class AlertWindow(AbstractWindow):

    def __init__(self, j: ImplementedWindow) -> None:
        super().__init__(j)

    def draw(self) -> None:
        self.draw_window("Janela de Aviso")
        self.draw_button("Ok")


def main() -> None:
    abs_window = DialogueWindow(Windows())
    abs_window.draw()
    abs_window = AlertWindow(Windows())
    abs_window.draw()
    print('-' * 40)

    abs_window = DialogueWindow(Linux())
    abs_window.draw()
    abs_window = AlertWindow(Linux())
    abs_window.draw()
    print('-' * 40)

    abs_window = DialogueWindow(MAC())
    abs_window.draw()
    abs_window = AlertWindow(MAC())
    abs_window.draw()


if __name__ == "__main__":
    main()