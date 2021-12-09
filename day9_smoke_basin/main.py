import os, sys
import numpy as np
from functools import partial

task_dir = os.path.dirname(__file__)
sys.path.append(f"{task_dir}/..")
from get_tasks import get_input, generate_readme, check_example


def parse_input(inputs: list[str]):
    return np.array([list(line.strip()) for line in inputs], dtype=int)


def part1(cave: np.ndarray) -> np.ndarray:
    centers = np.array([0, 0], dtype=int)
    mins = np.array([], dtype=int)
    for i in range(cave.shape[0]):
        for j in range(cave.shape[1]):
            if (here := cave[i, j]) == (
                win := cave[max(0, i - 1) : i + 2, max(0, j - 1) : j + 2]
            ).min():
                mins = np.append(mins, here)
                centers = np.vstack([centers, [i, j]])
    centers = np.delete(centers, 0, 0)
    print("The answer of part1 is:", (mins + 1).sum())
    return centers


def part2(cave: np.ndarray, centers_basins: np.ndarray):
    def get_dirs(center):
        i, j = center
        up = max(0, i - 1), j
        left = i, max(0, j - 1)
        down = min(i + 1, i_size), j
        right = i, min(j_size, j + 1)
        return up, left, down, right

    for idx, center in enumerate(centers_basins):
        queue = []
        i, j = center
        i_size, j_size = cave.shape
        i_size, j_size = i_size - 1, j_size - 1

        queue.append((i, j))
        cave[i, j] = idx + 11

        while queue:
            pos = queue.pop()
            for dir in get_dirs(pos):
                if cave[dir] < 9:
                    cave[dir] = idx + 11
                    queue.append(dir)
    print(
        "The answer of part2 is:",
        np.sort(np.unique(cave[np.where(cave > 10)], return_counts=1)[1])[-3:].prod(),
    )


if __name__ == "__main__":
    input, example = get_input(task_dir, 9)

    example_cave = parse_input(example)
    real_cave = parse_input(input)

    check_example(example_cave, part1)
    example_basins = part1(example_cave)
    check_part2 = partial(part2, example_cave)
    check_example(example_basins, check_part2)

    centers_basisns = part1(real_cave)
    part2(real_cave, centers_basisns)

    generate_readme(task_dir, 9)
