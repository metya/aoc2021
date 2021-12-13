import os, sys
import numpy as np

task_dir = os.path.dirname(__file__)
sys.path.append(f"{task_dir}/..")
from get_tasks import get_input, generate_readme, check_example


def update_step_count(step: np.ndarray) -> tuple[int, np.ndarray, bool]:
    acc = 0
    while len(np.where((step > 9) & (step < 1000))[0]) != 0:
        x, y = np.where((step > 9) & (step < 1000))
        for idx in range(len(x)):
            step[max(0, x[idx] - 1) : x[idx] + 2, max(0, y[idx] - 1) : y[idx] + 2] += 1
            step[x[idx], y[idx]] = 1000 + acc
            acc += 1
    return (
        len(step[step > 9]),
        np.where(step > 9, 0, step),
        len(step[step > 9]) == step.size,
    )


def part1(input: list[str]):
    octopuses = np.array([list(line.strip()) for line in input], dtype=int)
    sum_flashes = 0
    for _ in range(1, 101):
        octopuses += 1
        flashes, octopuses, _ = update_step_count(octopuses)
        sum_flashes += flashes
    print("The asnwer of part1 is:", sum_flashes)


def part2(input: list[str]):
    octopuses = np.array([list(line.strip()) for line in input], dtype=int)
    step = 0
    all_flash = False
    while not all_flash:
        octopuses += 1
        _, _, all_flash = update_step_count(octopuses)
        step += 1
    print("The answer if part2 is:", step)


if __name__ == "__main__":

    input, example = get_input(task_dir, 11)

    check_example(example, part1)
    check_example(example, part2)
    part1(input)
    part2(input)

    generate_readme(task_dir, 11)
