import os, sys
import numpy as np
from queue import PriorityQueue
from collections import defaultdict, deque

task_dir = os.path.dirname(__file__)
sys.path.append(f"{task_dir}/..")
from get_tasks import get_input, check_example, generate_readme


def get_dirs(center, i_size, j_size):
    i, j = center
    up = max(0, i - 1), j
    left = i, max(0, j - 1)
    down = min(i + 1, i_size), j
    right = i, min(j_size, j + 1)
    return up, left, down, right


def dijkstra(G, start=(0, 0), end=False, pq=True, star=False):
    i_s, j_s = G.shape[0] - 1, G.shape[1] - 1
    end = (i_s, j_s) if not end else end
    parents = {}
    q = PriorityQueue() if pq else deque()
    nodeCosts = defaultdict(lambda: float("inf"))
    nodeCosts[start] = 0
    if pq:
        q.put((0, start))
    else:
        q.append((0, start))

    def get_path(node):
        path = []
        while node != start:
            path.append(node)
            node = parents[node]
        path.append(start)
        return path[::-1]

    def estimate(end, node):
        return abs(end[0] - node[0]) + abs(end[1] - node[1])

    acc = 0
    while (q.qsize() if pq else len(q)) != 0:
        acc += 1
        _, node = q.get() if pq else q.popleft()
        if pq and node == end:
            print("With early stop!", acc)
            return get_path(node), nodeCosts[node]
        for adjNode in get_dirs(node, i_s, j_s):
            newCost = nodeCosts[node] + G[adjNode]
            if nodeCosts[adjNode] > newCost:
                parents[adjNode] = node
                nodeCosts[adjNode] = newCost
                if star:
                    newCost += estimate(end, adjNode)
                if pq:
                    q.put((newCost, adjNode))
                else:
                    q.append((newCost, adjNode))
    return get_path(end), nodeCosts[end]


def part1(input: list[str], verbose=True):
    ceiling = np.array([list(line) for line in input], dtype=int)
    _, cost = dijkstra(ceiling)
    if verbose:
        print("The answer of part1 is:", cost)


def part2(input: list[str], pq=True, star=False, verbose=True):
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
    _, cost = dijkstra(full_ceiling, pq=pq, star=star)
    if verbose:
        print("The answer of part2 is:", cost)


if __name__ == "__main__":
    input, example = get_input(task_dir, 15)

    check_example(example, part1)
    check_example(example, part2)
    part1(input)
    part2(input)

    generate_readme(task_dir, 15)
