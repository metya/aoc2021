from doctest import Example
import os, sys
from tabnanny import check

from numpy import poly

task_dir = os.path.dirname(__file__)
sys.path.append(f"{task_dir}/..")
from get_tasks import get_input, check_example, generate_readme
from collections import Counter, defaultdict


def parse(input: list[str]) -> tuple[str, dict]:
    template = input[0]
    instructions = {}
    for line in input[2:]:
        key, value = line.split(" -> ")
        instructions[(key[0], key[1])] = value
    return template, instructions


def polymerize(steps: int, template: str, instructions: dict) -> int:
    counter = Counter(template)
    combinations: defaultdict[tuple, int] = defaultdict(int)
    for i in range(len(template) - 1):
        combinations[(template[i], template[i + 1])] += 1
    for _ in range(steps):
        temp_combinations = combinations.copy()
        for comb in temp_combinations:
            counter[instructions[comb]] += temp_combinations[comb]
            combinations[comb] -= temp_combinations[comb]
            combinations[(comb[0], instructions[comb])] += temp_combinations[comb]
            combinations[(instructions[comb], comb[1])] += temp_combinations[comb]
    return max(counter.values()) - min(counter.values())


def part1(input: list[str]):
    print("The answer of part1 is:", polymerize(10, *parse(input)))


def part2(input: list[str]):
    print("The answer if part2 is:", polymerize(40, *parse(input)))


if __name__ == "__main__":
    input, example = get_input(task_dir, 14)

    check_example(example, part1)
    check_example(example, part2)

    part1(input)
    part2(input)

    generate_readme(task_dir, 14)
