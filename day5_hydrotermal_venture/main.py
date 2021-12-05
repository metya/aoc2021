import re
import os, sys
import numpy as np

task_dir = os.path.dirname(__file__)
sys.path.append(f"{task_dir}/..")
from get_tasks import generate_readme, check_example, get_input


def draw_lines(input: str, diag: bool = False) -> int:

    with open(f"{input}.txt", "r") as f:
        inp = f.readlines()

    coords = np.array(
        [
            np.array([(nums[0:2], nums[2:])], dtype=int)
            for nums in [re.findall("\d+", num) for num in inp]
        ]
    )
    size = coords.max()
    field = np.zeros([size + 1, size + 1])
    coords = coords.reshape(coords.shape[0], 2, 2)

    for cp in coords:
        if (p1 := cp[0][0]) == (cp[1][0]):
            field[min(cp[0][1], cp[1][1]) : max(cp[0][1], cp[1][1]) + 1, p1] += 1
        elif (p1 := cp[0][1]) == (cp[1][1]):
            field[p1, min(cp[0][0], cp[1][0]) : max(cp[0][0], cp[1][0]) + 1] += 1
        elif diag:
            mat = field[
                cp[:, 1].min() : cp[:, 1].max() + 1, cp[:, 0].min() : cp[:, 0].max() + 1
            ]
            if cp[1].sum() == cp[0].sum():
                np.fliplr(mat).flat[:: mat.shape[0] + 1] += 1
            else:
                mat.flat[:: mat.shape[0] + 1] += 1

    return np.count_nonzero(field > 1)


def part1(input: str):
    print("The answer of part1 is:", draw_lines(input, diag=False))


def part2(input: str):
    print("The answer of part2 is:", draw_lines(input, diag=True))


if __name__ == "__main__":
    get_input(task_dir, 5)

    check_example("example", part1)
    check_example("example", part2)
    part1("input")
    part2("input")

    generate_readme(task_dir, 5)
