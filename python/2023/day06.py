import functools
import math
import operator
from io import StringIO
from pathlib import Path

from python.utils import catchtime

input_path = Path(__file__).parents[2].joinpath("input/2023/day06.txt")

sample_input = StringIO(
    """\
Time:      7  15   30
Distance:  9  40  200
"""
)


def calc_ways(inputs: tuple[int, int]) -> int:
    time, dist = inputs
    first = (time - math.sqrt(time * time - 4 * dist)) / 2
    second = (time + math.sqrt(time * time - 4 * dist)) / 2

    if first.is_integer():
        first += 1
    if second.is_integer():
        second -= 1

    return math.floor(second) - math.ceil(first) + 1


def part1() -> int:
    with input_path.open() as f:
        times = [int(t) for t in f.readline().partition(":")[2].strip().split()]
        distances = [int(d) for d in f.readline().partition(":")[2].strip().split()]

    ways_to_win = map(calc_ways, zip(times, distances, strict=True))
    return functools.reduce(operator.mul, ways_to_win)


def part2() -> int:
    with input_path.open() as f:
        time = f.readline().partition(":")[2].strip().replace(" ", "")
        distance = f.readline().partition(":")[2].strip().replace(" ", "")

    return calc_ways((int(time), int(distance)))


if __name__ == "__main__":
    with catchtime() as ct:
        result = part1()
    print(result)
    print(ct.time)

    with catchtime() as ct:
        result = part2()
    print(result)
    print(ct.time)
