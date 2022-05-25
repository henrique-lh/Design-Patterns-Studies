class Aluno:

    def __init__(self, matricula: str = None, nome: str = None) -> None:
        self._matricula = matricula
        self._nome = nome

    @property
    def getNome(self) -> str:
        return self._nome

    @property
    def getMatricula(self) -> str:
        return self._matricula
