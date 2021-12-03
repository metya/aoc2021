import os, sys

task_dir = os.path.dirname(__file__)
sys.path.append(f"{task_dir}/..")
from get_tasks import get_input

measures, example = get_input(task_dir, 1)
# print(example)


def part1(input):
    counter = 0
    temp = max(int(m) for m in input)
    for measure in input:
        if int(measure) > temp:
            counter += 1
        temp = int(measure)

    print("The answer of part1 is:", counter)


def check_part1(example):
    part1(example)


def part2(input):
    input = [int(m) for m in input]
    counter = 0
    temp = sum(input[0:3])
    for ind in range(len(input) - 2):
        if sum(input[ind : ind + 3]) > temp:
            counter += 1
        temp = sum(input[ind : ind + 3])

    print("The answer of part2 is:", counter)


def check_part2(example):
    part2(example)


if __name__ == "__main__":
    check_part1(example)
    part1(measures)
    check_part2(example)
    part2(measures)
