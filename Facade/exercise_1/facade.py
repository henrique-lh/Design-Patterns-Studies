from typing import Dict
from curso import Curso
from aluno import Aluno
from escola import Escola
from turma import Turma

class Facade:
    
    registered_cursos: Dict[str, Turma] = dict()

    @classmethod
    def matricular(cls, codAluno: str, codCurso: str) -> None:
        if codCurso not in cls.registered_cursos:
            cn = codCurso.split('_')[0]
            cls.registered_cursos[codCurso] = Turma()
            c: Curso = Escola.getCurso(codigo=cn)
            cls.registered_cursos[codCurso].setCurso(c)
        rex: Aluno = Escola.getAluno(codigo=codAluno)
        cls.registered_cursos[codCurso].addAluno(rex)

    @classmethod
    def exibitStatus(cls, turma_id: str) -> None:
        alunos = cls.registered_cursos[turma_id].getAlunos
        print(f"Turma: {cls.registered_cursos[turma_id].getCurso.getNome}({turma_id.split('_')[1]})")
        for aluno in alunos:
            print(f"Nome do aluno: {aluno.getNome:>12} | N° de matricula: {aluno.getMatricula:>5}")
        print()