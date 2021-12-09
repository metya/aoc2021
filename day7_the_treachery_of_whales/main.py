import os, sys
import numpy as np

task_dir = os.path.dirname(__file__)
sys.path.append(f"{task_dir}/..")
from get_tasks import get_input, generate_readme, check_example


def part1(input: list[str]):
    positions = np.fromstring(input[0], sep=",", dtype=int)
    a = np.abs(positions - np.floor(np.median(positions))).sum()
    print(f"The answer of part1 is: {a}")


def part2(input: list[str]):
    positions = np.fromstring(input[0], sep=",", dtype=int)
    a = np.abs(positions - np.floor(np.mean(positions)))
    a = np.array([np.arange(n + 1).sum() for n in a]).sum()
    print(f"The answer of part2 is: {a}")


if __name__ == "__main__":
    input, example = get_input(task_dir, 7)

    check_example(example, part1)
    check_example(example, part2)
    part1(input)
    part2(input)

    generate_readme(task_dir, 7)
