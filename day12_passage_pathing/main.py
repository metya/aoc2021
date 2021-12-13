from doctest import Example
import os, sys

task_dir = os.path.dirname(__file__)
sys.path.append(f"{task_dir}/..")
from get_tasks import get_input, check_example, generate_readme
from collections import deque, defaultdict


def parse(input: list[str]) -> dict:
    in_map_cave = defaultdict(list)
    for line in input:
        a, b = line.split("-")
        in_map_cave[a].append(b)
        if a != "start" and b != "end":
            in_map_cave[b].append(a)
    return dict(in_map_cave)


def findpaths(map_cave: dict, twice=False) -> tuple[int, list]:
    paths = []
    path = ["start"]
    q = deque([path])
    state_q = deque([False])
    while q:
        path = q.popleft()
        double_visited = state_q.popleft()
        if path[-1] == "end":
            paths.append(path)
            continue
        for cave in map_cave[path[-1]]:
            if not (cave.islower() and (cave in path)):
                q.append(path + [cave])
                state_q.append(double_visited)
            elif not double_visited and twice:
                state_q.append(True)
                q.append(path + [cave])
    return len(paths), paths


def findpaths_first_version(map_cave: dict) -> tuple[int, list]:
    paths = []
    path = ["start"]
    q = deque([path])
    while q:
        path = q.popleft()
        if path[-1] == "end":
            paths.append(path)
            continue
        for cave in map_cave[path[-1]]:
            if not (cave.islower() and (cave in path)):
                newpath = path.copy()
                newpath.append(cave)
                q.append(newpath)
    return len(paths), paths


def part1(input: list[str]):
    l, _ = findpaths(parse(input))
    print("The answer of part1 is:", l)


def part2(input: list[str]):
    l, _ = findpaths(parse(input), twice=True)
    print("The answer of part2 is:", l)


if __name__ == "__main__":
    input, example = get_input(task_dir, 12)

    check_example(example, part1)
    check_example(example, part2)
    part1(input)
    part2(input)

    generate_readme(task_dir, 12)
