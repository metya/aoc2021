import os, sys
import numpy as np

task_dir = os.path.dirname(__file__)
sys.path.append(f"{task_dir}/..")
from get_tasks import get_input, check_example, generate_readme


def folding(input: list[str]) -> tuple[int, np.ndarray]:
    coords = np.array(
        [
            (line.split(",")[1], line.split(",")[0])
            for line in input
            if len(line) > 1 and len(line) < 12
        ],
        dtype=int,
    )
    instructions = [line[11:].split("=") for line in input if line.startswith("f")]
    x, y = 0, 0
    for inst in instructions:
        match inst:
            case ["y", c]: x = int(c) * 2 + 1
            case ["x", c]: y = int(c) * 2 + 1
        if x != 0 and y != 0: paper = np.zeros((x, y), dtype=np.int8); break
    paper[coords[:, 0], coords[:, 1]] = 1
    for step, inst in enumerate(instructions):
        match inst:
            case ["y", c]: paper = paper[: int(c)] + np.flipud(paper[int(c) + 1 :])
            case ["x", c]: paper = paper[:, : int(c)] + np.fliplr(paper[:, int(c) + 1 :])
        if step == 0:
            part1 = np.where(paper > 0, 1, 0).sum()
    part2 = np.where(paper > 0, "#", ".")
    return part1, part2


def part1(input: list[str]):
    part1, _ = folding(input)
    print("The anwer of part1 is:", part1)


def part2(input: list[str]):
    _, part2 = folding(input)
    print("The answer of part2 is:\n")
    for line in part2:
        print("".join(line))


if __name__ == "__main__":
    input, example = get_input(task_dir, 13)

    check_example(example, part1)
    part1(input)
    part2(input)

    generate_readme(task_dir, 13)
