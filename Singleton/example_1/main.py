from __future__ import annotations

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs) -> Singleton:
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Logger(metaclass=Singleton):
    pass


def main() -> None:

    s1 = Logger()
    s2 = Logger()

    if id(s1) == id(s2):
        print("s1 and s2 has the same ID")
    else:
        print("s1 and s2 has different ID's")

if __name__ == "__main__":
    main()