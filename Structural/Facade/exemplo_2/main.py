from __future__ import annotations


class _CPU:

    def freeze(self) -> None:
        print("Freezing processor")

    def jump(self, position: int) -> None:
        print("Jumping to:", position)

    def execute(self) -> None:
        print("Executing")


class _Memory:

    def load(self, position: str, data: str) -> None:
        print(f"Loading from {position} data: {data}")


class _SolidStateDrive:

    def read(self, lba, size) -> str:
        return f"Some data from sector {lba} with size {size}"


class ComputerFacade:

    def __init__(self) -> None:
        self._cpu: _CPU = _CPU()
        self._memory: _Memory = _Memory()
        self._ssd: _SolidStateDrive = _SolidStateDrive()

    def start(self) -> None:
        self._cpu.freeze()
        self._memory.load("0x00", self._ssd.read("100", "1024"))
        self._cpu.jump("0x00")
        self._cpu.execute()


def main():
    
    computer_facade = ComputerFacade()
    computer_facade.start()


if __name__ == "__main__":
    main()