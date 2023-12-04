import re
from io import StringIO
from pathlib import Path

input_path = Path(__file__).parents[2].joinpath("input/2023/day03.txt")

sample_input = StringIO(
    """\
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""
)


def part1() -> int:
    def check_valid(match: re.Match[str], line_length: int, source: str) -> bool:
        value, start, end = match.group(0), match.start(), match.end()
        print(f"{line_length=}")
        print(value)
        val_length = len(value)
        condition = True
        if start != 0:
            condition &= source[start - 1] == "."
            print("1st: ", condition)
        if end != len(source):
            condition &= source[end] == "."
            print("2nd: ", condition)
        if start > line_length:
            condition &= source[start - line_length - 1 : end - line_length + 1] == "." * (val_length + 2)
            print("3rd: ", condition)
        if end <= len(source) - line_length:
            print(source[start + line_length - 1 : end + line_length + 1])
            condition &= source[start + line_length - 1 : end + line_length + 1] == "." * (val_length + 2)
            print("4th: ", condition)
        return condition

    with sample_input as f:
        source = f.read()
        line_length = source.index("\n")
        source = source.replace("\n", "")
    data = re.finditer(r"\d+", source)
    data = [int(match.group(0)) for match in data if check_valid(match, line_length, source)]
    print(data)
    return sum(data)


def part2() -> int:
    ...


if __name__ == "__main__":
    print(part1())
    # print(part2())
