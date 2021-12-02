import os, sys
from collections import defaultdict
from typing import Callable

task_dir = os.path.dirname(__file__)
sys.path.append(f"{task_dir}/..")
from get_tasks import get_input

input, example = get_input(task_dir, 2)


def check_example(example: list[str], part: Callable):
    part(example)


def part1(input: list[str]):
    path: defaultdict = defaultdict(int)
    for go in input:
        direction, value = go.split()
        if direction == "forward":
            path["forward"] += int(value)
        if direction == "down":
            path["depth"] += int(value)
        if direction == "up":
            path["depth"] -= int(value)
    print("The answer of part1 is:", path["forward"] * path["depth"])


def part2(input: list[str]):
    path = defaultdict(int)
    path["aim"] = 0
    for go in input:
        direction, value = go.split()
        if direction == "forward":
            path["forward"] += int(value)
            path["depth"] += int(value) * path["aim"]
        if direction == "down":
            path["aim"] += int(value)
        if direction == "up":
            path["aim"] -= int(value)
    print("The answer of part1 is:", path["forward"] * path["depth"])


if __name__ == "__main__":
    check_example(example, part1)
    part1(input)
    check_example(example, part2)
    part2(input)
