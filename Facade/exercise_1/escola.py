from typing import List, Tuple
from curso import Curso
from aluno import Aluno

def _set_up_cursos() -> List[Tuple[str]]:
    return (
        [
            ("Padrões de Projeto", "123654"), ("Estruturas de Dados", "002320"), ("Sistemas Operacionais", "741258"),
            ("Eletromagnetismo", "521456"), ("Programação Orientada a Objetos", "452321")
        ]
    )

def _set_up_alunos() -> List[Tuple[str]]:
    return (
        [
            ("123", "Luis"), ("456", "Julia"), ("789", "Carlos"), ("741", "Fernando"), 
            ("852", "Adriana"), ("159", "Márcio"),("842", "Manoela"), ("956", "Jonas"), ("523", "Silvany"),
            ("001", "Hermano"), ("035", "Tarcisio"), ("751", "João"),
            ("000", "Lima"), ("006", "Lemos"), ("667", "Gomes"),
        ]
    )


class Escola:

    _cursos: List[Curso] = [Curso(curso, id) for curso, id in _set_up_cursos()]
    _alunos: List[Aluno] = [Aluno(matricula, aluno) for matricula, aluno in _set_up_alunos()]

    @classmethod
    def getCurso(cls, codigo: str) -> Curso:
        for curso in cls._cursos:
            if curso.get_id == codigo:
                return curso

    @classmethod
    def getAluno(cls, codigo: str) -> Aluno:
        for aluno in cls._alunos:
            if aluno.getMatricula == codigo:
                return aluno
