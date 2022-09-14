"""Problem: https://brizeno.wordpress.com/category/padroes-de-projeto/proxy/"""

import random
random.seed(159)


class UsersDB:

    def __init__(self) -> None:
        self.__total_users = random.randint(1, 100)
        self.__conected_users = random.randint(1, self.__total_users - 1)

    @property
    def total_users(self) -> int:
        return self.__total_users

    @property
    def conected_users(self) -> int:
        return self.__conected_users


class ProxyDB(UsersDB):

    def __init__(self, user_name: str, password: str) -> None:
        super().__init__()
        self._user_name = user_name
        self._password = password

    def total_users(self) -> int:
        if self.__get_access():
            return super().total_users
        return None

    def conected_users(self) -> int:
        if self.__get_access():
            return super().conected_users
        return None

    def __get_access(self) -> bool:
        return self._user_name == 'admin' and self._password == 'admin123'


def main() -> None:
    print('Hacking accessing...')
    db = ProxyDB('Hacker', '1234')
    print(f'Total of users on the system: {db.total_users()}')
    print(f'Total of connceted users on the system: {db.conected_users()}')

    print()

    print('Admin accessing...')
    db = ProxyDB('admin', 'admin123')
    print(f'Total of users on the system: {db.total_users()}')
    print(f'Total of connceted users on the system: {db.conected_users()}')

if __name__ == "__main__":
    main()
