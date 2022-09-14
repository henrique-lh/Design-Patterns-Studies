from abc import ABCMeta, abstractmethod, abstractstaticmethod

class IDepartment(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, employees: int) -> None:
        """ Implement in child class """

    @abstractstaticmethod
    def print_department():
        """ implement in child class """


class Accouting(IDepartment):
    """ Child of the tree """

    def __init__(self, employees: int) -> None:
        self.employees = employees

    def print_department(self) -> None:
        print(f"Accounting Department: {self.employees}")

class Development(IDepartment):
    """ Child of the tree """

    def __init__(self, employees: int) -> None:
        self.employees = employees

    def print_department(self) -> None:
        print(f"Development Department: {self.employees}")


class ParentDepartment(IDepartment):

    def __init__(self, employees: int) -> None:
        self.employees = employees
        self.base_employeese = employees
        self.sub_depts = []

    def add(self, dept: IDepartment) -> None:
        self.sub_depts.append(dept)
        self.employees += dept.employees

    def remove(self, dept: IDepartment) -> None:
        self.sub_depts.remove(dept)

    def print_department(self) -> None:
        print("Parent Department")
        print(f"Parent Department Base Employees: {self.base_employeese}")
        for dept in self.sub_depts:
            dept.print_department()
        print(f"Total of employees: {self.employees}")

def main() -> None:
    dept1 = Accouting(200)
    dept2 = Development(300)
    parent_dept = ParentDepartment(30)
    parent_dept.add(dept=dept1)
    parent_dept.add(dept=dept2)

    parent_dept.print_department()


if __name__ == "__main__":
    main()