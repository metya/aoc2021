import os, sys
import numpy as np
from queue import PriorityQueue
from collections import defaultdict

task_dir = os.path.dirname(__file__)
sys.path.append(f"{task_dir}/..")
from get_tasks import get_input, check_example, generate_readme


def get_dirs(center, i_size, j_size, going_up=False, going_down=False):
    i, j = center
    up = max(0, i - 1), j
    left = i, max(0, j - 1)
    down = min(i + 1, i_size), j
    right = i, min(j_size, j + 1)
    if going_up:
        return up, left
    if going_down:
        return down, right
    return up, left, down, right


def dijkstra(G, start=(0, 0), end=False, up=False, down=False):
    i_s, j_s = G.shape[0] - 1, G.shape[1] - 1
    end = (i_s, j_s) if not end else end
    path = []
    parents = {}
    visited = set()
    pq = PriorityQueue()
    nodeCosts = defaultdict(lambda: float("inf"))
    nodeCosts[start] = 0
    pq.put((0, start))

    def get_path(node):
        while node != start:
            path.append(node)
            prev_node = parents[node]
            node = prev_node
        path.append(start)
        return path[::-1]

    while pq:
        _, node = pq.get()
        if node == end:
            print("Get end!")
            return get_path(node), nodeCosts[end]
        visited.add(node)
        for adjNode in get_dirs(node, i_s, j_s, up, down):
            if adjNode in visited:
                continue
            newCost = nodeCosts[node] + G[adjNode]
            if nodeCosts[adjNode] > newCost:
                parents[adjNode] = node
                nodeCosts[adjNode] = newCost
                pq.put((newCost, adjNode))

    print("Can't get to the end!")
    return get_path(node), nodeCosts


def part1(input: list[str]):
    ceiling = np.array([list(line) for line in input], dtype=int)
    _, cost = dijkstra(ceiling, down=True)
    print("The answer of part1 is:", cost)


def part2(input: list[str]):
    ceiling = np.array([list(line) for line in input], dtype=int)
    full_ceiling = ceiling.copy()
    for step in range(1, 5):
        left_ceiling = ceiling + step
        left_ceiling[left_ceiling > 9] -= 9
        full_ceiling = np.hstack([full_ceiling, left_ceiling])
    line_ceiling = full_ceiling.copy()
    for step in range(1, 5):
        down_ceiling = line_ceiling + step
        down_ceiling[down_ceiling > 9] -= 9
        full_ceiling = np.vstack([full_ceiling, down_ceiling])
    _, cost = dijkstra(full_ceiling, down=True)
    print("The answer of part2 is:", cost)


if __name__ == "__main__":
    input, example = get_input(task_dir, 15)

    check_example(example, part1)
    check_example(example, part2)
    part1(input)
    part2(input)

    generate_readme(task_dir, 15)
