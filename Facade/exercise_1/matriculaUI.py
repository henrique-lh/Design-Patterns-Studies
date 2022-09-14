from facade import Facade

class MatriculaUI:

    def matricular(self, codAluno: str, codCurso: str) -> None:
        print("-" * 50)
        print("Matricula por interface UI selecionada.")
        Facade.matricular(codAluno, codCurso)
        print("Aluno matriculado com sucesso!")

    def exibitStatus(self, turma: str) -> None:
        Facade.exibitStatus(turma)
