import operator
from itertools import chain
from pathlib import Path


def part1():
    total = 0

    with Path(__file__).parent.joinpath("input/input.txt").open() as f:
        for line in f:
            integers = [i for i in line if i.isdigit()]
            total += int(integers[0] + integers[-1])

    print(total)


def part2():
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

    total = 0

    with Path(__file__).parent.joinpath("input/input.txt").open() as f:
        for line in f:
            found_ints = [
                (search_str, line.find(search_str), line.rfind(search_str))
                for search_str in chain.from_iterable(num_lookup.items())
                if search_str in line
            ]

            first_str, first_index, _ = min(found_ints, key=operator.itemgetter(1))
            second_str, _, second_index = max(found_ints, key=operator.itemgetter(2))

            first = line[first_index : first_index + len(first_str)]
            second = line[second_index : second_index + len(second_str)]

            result = "".join(
                (component if component.isdigit() else num_lookup[component]) for component in (first, second)
            )

            total += int(result)

    print(total)


if __name__ == "__main__":
    part1()
    part2()
