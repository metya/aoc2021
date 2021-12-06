from doctest import Example
import os, sys
import numpy as np

task_dir = os.path.dirname(__file__)
sys.path.append(f"{task_dir}/..")
from get_tasks import get_input, check_example, generate_readme


def grow(input: list[str], days) -> int:
    # parse data to array with days
    state = np.fromstring(input[0], sep=",", dtype=int)
    counts = np.zeros(9, dtype=int)
    day_left, count = np.unique(state, return_counts=1)
    counts[day_left] += count

    for day in range(days):
        counts[(day + 7) % 9] += counts[day % 9]
    return counts.sum()


def part1(input: list[str]):
    print('The answer of part1 is:', grow(input, 80))


def part2(input: list[str]):
    print('The answer of part2 is:', grow(input, 256))


if __name__ == "__main__":
    input, example = get_input(task_dir, 6)
    
    check_example(example, part1)
    check_example(example, part2)
    part1(input)
    part2(input)
    
    generate_readme(task_dir, 6)
