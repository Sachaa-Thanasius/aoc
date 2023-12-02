import operator
from pathlib import Path

from python.utils import catchtime

input_path = Path(__file__).parents[2].joinpath("input/2023/day01.txt")


def part1() -> int:
    total = 0

    with input_path.open() as f:
        for line in f:
            integers = [i for i in line if i.isdigit()]
            total += int(integers[0] + integers[-1])

    return total


def part2() -> int:
    num_lookup = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    num_list = list(num_lookup.keys()) + list(num_lookup.values())

    get_index_1 = operator.itemgetter(1)
    get_index_2 = operator.itemgetter(2)

    total = 0

    with input_path.open() as f:
        for line in f:
            found_ints = [
                (search_str, line.find(search_str), line.rfind(search_str))
                for search_str in num_list
                if search_str in line
            ]

            first, _, _ = min(found_ints, key=get_index_1)
            second, _, _ = max(found_ints, key=get_index_2)

            result = "".join(
                (component if component.isdigit() else num_lookup[component]) for component in (first, second)
            )

            total += int(result)

    return total


if __name__ == "__main__":
    with catchtime() as ct:
        result = part1()

    with catchtime() as ct2:
        result2 = part2()

    print(result, ct.time)
    print(result2, ct2.time)
