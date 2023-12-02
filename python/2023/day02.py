import re
from io import StringIO
from pathlib import Path
from typing import Any

from python.utils import catchtime

input_path = Path(__file__).parents[2].joinpath("input/2023/day02.txt")

sample_input = StringIO(
    """\
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""
)

COLOUR_PATTERN = re.compile(r"(?P<count>\d+) (?P<colour>red|green|blue)")
RED_PTRN = re.compile(r"(?P<count>\d+) red")
GREEN_PTRN = re.compile(r"(?P<count>\d+) green")
BLUE_PTRN = re.compile(r"(?P<count>\d+) blue")


def part1() -> int:
    def check_valid(count: Any, colour: str) -> bool:  # noqa: ANN401
        return (
            (colour == "red" and int(count) <= 12)
            or (colour == "green" and int(count) <= 13)
            or (colour == "blue" and int(count) <= 14)
        )

    with input_path.open() as f:
        data = (line.partition(":") for line in f)
        data = ((int(game.partition(" ")[2]), raw) for game, _, raw in data)
        data = (
            game_num
            for game_num, raw in data
            if all(check_valid(**match.groupdict()) for match in re.finditer(COLOUR_PATTERN, raw))
        )

        return sum(data)


def part2() -> int:
    def max_count(pattern: re.Pattern[str], line: str) -> int:
        return max(int(match.group("count")) for match in re.finditer(pattern, line))

    with input_path.open() as f:
        data = ((max_count(RED_PTRN, line), max_count(GREEN_PTRN, line), max_count(BLUE_PTRN, line)) for line in f)
        return sum(red * green * blue for red, green, blue in data)


if __name__ == "__main__":
    with catchtime() as ct:
        result = part1()

    with catchtime() as ct2:
        result2 = part2()

    print(result, ct.time)
    print(result2, ct2.time)
