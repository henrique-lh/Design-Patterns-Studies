from typing import List
from curso import Curso
from aluno import Aluno


class Turma:
    
    def __init__(self) -> None:
        self._alunos: List[Aluno] = []
        self._curso: Curso = None

    def addAluno(self, novo_aluno: Aluno) -> None:
        self._alunos.append(novo_aluno)

    def setCurso(self, novo_curso: Curso) -> None:
        self._curso = novo_curso

    @property
    def getAlunos(self) -> List[Aluno]:
        return self._alunos

    @property
    def getCurso(self) -> Curso:
        return self._curso

