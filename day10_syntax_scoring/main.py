import os, sys

task_dir = os.path.dirname(__file__)
sys.path.append(f"{task_dir}/..")
from get_tasks import get_input, check_example, generate_readme


def solve(input: list[str]) -> tuple[int, int]:

    braces = {")": "(", "}": "{", "]": "[", ">": "<"}
    reverse_braces = {"(": ")", "{": "}", "[": "]", "<": ">"}
    illegal_points = {")": 3, "}": 1197, "]": 57, ">": 25137}
    completion_points = {")": 1, "}": 3, "]": 2, ">": 4}

    scores = []
    sum = 0

    for line in input:
        score = 0
        stack = []
        not_corrapted = True
        for char in line.strip():
            if char in braces.values():
                stack.append(char)
            else:
                if braces[char] == stack[-1]:
                    stack.pop()
                else:
                    sum += illegal_points[char]
                    not_corrapted = False
                    break
        if not_corrapted:
            while stack:
                score = score * 5 + completion_points[reverse_braces[stack.pop()]]
            scores.append(score)
    print("The anwer of part1 is:", sum)
    print("The anser of part2 is:", sorted(scores)[int(len(scores) / 2)])
    return sum, sorted(scores)[int(len(scores) / 2)]


if __name__ == "__main__":
    input, example = get_input(task_dir, 10)

    check_example(example, solve)
    solve(input)

    generate_readme(task_dir, 10)
