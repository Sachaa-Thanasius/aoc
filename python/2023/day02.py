import re
from io import StringIO
from pathlib import Path

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

RED_PTRN = re.compile(r"(?P<count>\d+) (?P<color>red)")
GREEN_PTRN = re.compile(r"(?P<count>\d+) (?P<color>green)")
BLUE_PTRN = re.compile(r"(?P<count>\d+) (?P<color>blue)")


def part1() -> int:
    with input_path.open() as f:
        data = (line.partition(":") for line in f)
        data = [(game.partition(" ")[2], raw) for game, _, raw in data]
        all_game_nums = {int(game_num) for game_num, _ in data}
        red_data = (
            int(game_num)
            for game_num, raw in data
            for match in re.finditer(RED_PTRN, raw)
            if int(match.group("count")) > 12
        )
        green_data = (
            int(game_num)
            for game_num, raw in data
            for match in re.finditer(GREEN_PTRN, raw)
            if int(match.group("count")) > 13
        )
        blue_data = (
            int(game_num)
            for game_num, raw in data
            for match in re.finditer(BLUE_PTRN, raw)
            if int(match.group("count")) > 14
        )

        return sum(all_game_nums.difference(red_data, green_data, blue_data))


def part2() -> int:
    with input_path.open() as f:
        data = f.readlines()
        red_data = (max(int(match.group("count")) for match in re.finditer(RED_PTRN, line)) for line in data)
        green_data = (max(int(match.group("count")) for match in re.finditer(GREEN_PTRN, line)) for line in data)
        blue_data = (max(int(match.group("count")) for match in re.finditer(BLUE_PTRN, line)) for line in data)

        return sum(red * green * blue for red, green, blue in zip(red_data, green_data, blue_data, strict=True))


if __name__ == "__main__":
    with catchtime() as ct:
        print(part1())
    print(ct.time)
    with catchtime() as ct:
        print(part2())
    print(ct.time)
