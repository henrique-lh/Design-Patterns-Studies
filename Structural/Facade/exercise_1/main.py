import time
import os
from matriculaCLI import MatriculaCLI
from matriculaGUI import MatriculaGUI
from matriculaUI import MatriculaUI


def time_clear() -> None:
    time.sleep(10)
    os.system("clear")

def set_up(matricula_ui, matricula_cli, matricula_gui) -> None:

    matricula_ui.matricular("123", "123654_A")
    matricula_ui.matricular("123", "741258_A")
    matricula_ui.matricular("123", "521456_B")
    matricula_ui.matricular("123", "452321_B")
    matricula_ui.matricular("123", "002320_A")

    matricula_cli.matricular("456", "123654_B")
    matricula_cli.matricular("456", "741258_B")
    matricula_cli.matricular("456", "521456_A")
    matricula_cli.matricular("456", "452321_A")
    matricula_cli.matricular("456", "002320_B")

    matricula_gui.matricular("789", "123654_A")
    matricula_gui.matricular("789", "741258_B")
    matricula_gui.matricular("789", "521456_A")
    matricula_gui.matricular("789", "452321_B")
    matricula_gui.matricular("789", "002320_B")

    matricula_ui.matricular("741", "123654_B")
    matricula_ui.matricular("741", "741258_A")
    matricula_ui.matricular("741", "521456_B")
    matricula_ui.matricular("741", "452321_A")
    matricula_ui.matricular("741", "002320_A")

    matricula_cli.matricular("852", "123654_A")
    matricula_cli.matricular("852", "741258_A")
    matricula_cli.matricular("852", "521456_A")
    matricula_cli.matricular("852", "452321_A")
    matricula_cli.matricular("852", "002320_A")

    matricula_gui.matricular("159", "123654_B")
    matricula_gui.matricular("159", "741258_B")
    matricula_gui.matricular("159", "521456_B")
    matricula_gui.matricular("159", "452321_B")
    matricula_gui.matricular("159", "002320_A")

    matricula_ui.matricular("842", "123654_A")
    matricula_ui.matricular("842", "741258_B")
    matricula_ui.matricular("842", "521456_B")
    matricula_ui.matricular("842", "452321_B")
    matricula_ui.matricular("842", "002320_A")

    matricula_cli.matricular("956", "123654_A")
    matricula_cli.matricular("956", "741258_A")
    matricula_cli.matricular("956", "521456_A")
    matricula_cli.matricular("956", "452321_B")
    matricula_cli.matricular("956", "002320_B")

    matricula_gui.matricular("523", "123654_A")
    matricula_gui.matricular("523", "741258_B")
    matricula_gui.matricular("523", "521456_A")
    matricula_gui.matricular("523", "452321_A")
    matricula_gui.matricular("523", "002320_A")

    matricula_ui.matricular("001", "123654_A")
    matricula_ui.matricular("001", "741258_A")
    matricula_ui.matricular("001", "521456_B")
    matricula_ui.matricular("001", "452321_A")
    matricula_ui.matricular("001", "002320_A")

def main() -> None:
    matricula_ui = MatriculaUI()
    matricula_gui = MatriculaGUI()
    matricula_cli = MatriculaCLI()

    set_up(matricula_ui=matricula_ui, matricula_cli=matricula_cli, matricula_gui=matricula_gui)
    time_clear()

    t_1 = ["123654_A", "123654_B", "741258_A", "741258_B",]
    for t in t_1:
        matricula_ui.exibitStatus(t)

    t_2 = ["002320_A", "002320_B", "521456_A",]
    for t in t_2:
        matricula_gui.exibitStatus(t)

    t_3 = ["521456_B", "452321_A", "452321_B"]
    for t in t_3:
        matricula_cli.exibitStatus(t)


if __name__ == "__main__":
    main()