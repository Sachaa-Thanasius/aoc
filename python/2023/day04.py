import math
from collections import Counter
from io import StringIO
from pathlib import Path

input_path = Path(__file__).parents[2].joinpath("input/2023/day04.txt")

sample_input = StringIO(
    """\
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""
)


def part1() -> int:
    with input_path.open() as f:
        # Remove the card num prefix and split the data into two halves.
        data = (line[line.index(":") :].partition("|") for line in f)

        # Split each half into a list.
        data = ((winning.strip().split(), mine.strip().split()) for (winning, _, mine) in data)

        # Get the total winning cards from the side owned by the elf.
        data = (len(set(winning).intersection(mine)) for winning, mine in data)

        # Calculate the points based on those card numbers.
        data = ((math.pow(2, num_winners - 1) if num_winners >= 1 else 0) for num_winners in data)

        return int(sum(data))


def part2() -> int:
    with input_path.open() as f:
        data = ((card_num, line[line.index(":") :].partition("|")) for card_num, line in enumerate(f, start=1))
        data = ((card_num, (winning.strip().split(), mine.strip().split())) for card_num, (winning, _, mine) in data)
        data = ((card_num, len(set(winning).intersection(mine))) for card_num, (winning, mine) in data)

        data_counter = Counter(dict(data))
        copy_counter: Counter[int] = Counter()
        for card_num, num_winner in data_counter.items():
            new_update = list(range(card_num + 1, card_num + num_winner + 1)) * (copy_counter.get(card_num, 0) + 1)
            copy_counter.update(new_update)

        copy_counter.update({card_num: 1 for card_num in data_counter})
        return sum(copy_counter.values())


if __name__ == "__main__":
    print(part1())
    print(part2())
