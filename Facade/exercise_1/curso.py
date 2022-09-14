class Curso:

    def __init__(self, nome: str = None, id: str = None) -> None:
        self._nome = nome
        self._id = id

    @property
    def getNome(self) -> str:
        return self._nome

    @property
    def get_id(self) -> str:
        return self._id
