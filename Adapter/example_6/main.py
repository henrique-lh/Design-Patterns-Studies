from __future__ import annotations
import math

class RoundHole:

    def __init__(self, radius: int) -> int:
        self._radius = radius

    @property
    def getRadius(self) -> int:
        return self._radius

    def fits(self, peg: RoundPeg) -> bool:
        return self._radius >= peg.getRadius


class RoundPeg:

    def __init__(self, radius: int) -> None:
        self._radius = radius

    @property
    def getRadius(self) -> int:
        return self._radius


class SquarePeg:

    def __init__(self, width: int) -> None:
        self._width = width

    @property
    def getWidth(self) -> int:
        return self._width


class SquarePegAdapter(RoundPeg):

    __peg: SquarePeg

    def __init__(self, peg: SquarePeg) -> None:
        self.__peg = peg

    @property
    def getRadius(self) -> float:
        return self.__peg.getWidth * math.sqrt(2) / 2


def main() -> None:
    hole = RoundHole(5)
    rpeg = RoundPeg(5)
    print(f"Does rpget = 5 fits in hole? {hole.fits(rpeg)}") # True

    small_sqpeg = SquarePeg(5)
    large_sqpeg = SquarePeg(10)
    # print(f"Does small_sqpeg = 5 fits in hole? {hole.fits(small_sqpeg)}") # This won't work (incompatible types)

    small_sqpeg_adapter = SquarePegAdapter(small_sqpeg)
    large_sqpeg_adapter = SquarePegAdapter(large_sqpeg)
    print(f"Does small_sqpeg_adapter = 5 fits in hole? {hole.fits(small_sqpeg_adapter)}")
    print(f"Does large_sqpeg_adapter = 10 fits in hole? {hole.fits(large_sqpeg_adapter)}")

if __name__ == "__main__":
    main()