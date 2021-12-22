import os, sys

task_dir = os.path.dirname(__file__)
sys.path.append(f"{task_dir}/..")
from get_tasks import get_input, generate_readme, check_example, bench
from itertools import product
from functools import cache
from collections import Counter


def virgin_warmup_game(player1=0, player2=0, pos1=4, pos2=8):
    roll = 1
    step = 0
    while not (player1 >= 1000 or player2 >= 1000):
        if step % 2 == 0:
            pos1 = 10 if (s := (sum(range(roll, roll + 3)) + pos1) % 10) == 0 else s
            player1 += pos1
        else:
            pos2 = 10 if (s := (sum(range(roll, roll + 3)) + pos2) % 10) == 0 else s
            player2 += pos2
        roll += 3
        step += 3
        roll = roll % 100 if roll > 100 else roll
    return min(player1, player2) * step


outcomes = Counter(map(sum, product([1, 2, 3], [1, 2, 3], [1, 2, 3])))

@cache
def chad_dirac_dice(player1=0, player2=0, pos1=4, pos2=8):
    wins1, wins2 = 0, 0
    if player1 >= 21:
        return 1, 0
    if player2 >= 21:
        return 0, 1
    for s, c in outcomes.items():
        npos1 = 10 if (np := (s + pos1) % 10) == 0 else np
        a, b = chad_dirac_dice(player2, player1 + npos1, pos2, npos1)
        wins1 += b*c
        wins2 += a*c
    return wins1, wins2


@bench
def part1(input):
    pos1 = int(input[0][-1])
    pos2 = int(input[1][-1])
    print("The answer of part1 is:", virgin_warmup_game(pos1=pos1, pos2=pos2))


@bench
def part2(input):
    pos1 = int(input[0][-1])
    pos2 = int(input[1][-1])
    print("The answer of part2 is:", max(chad_dirac_dice(pos1=pos1, pos2=pos2)))


if __name__ == "__main__":
    input, example = get_input(task_dir, 21)

    check_example(example, part1)
    check_example(example, part2)

    part1(input)
    part2(input)

    generate_readme(task_dir, 21)
