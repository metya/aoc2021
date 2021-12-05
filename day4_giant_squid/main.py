import os, sys
import numpy as np

task_dir = os.path.dirname(__file__)
sys.path.append(f"{task_dir}/..")
from get_tasks import get_input, check_example, generate_readme


def parse_input(input: str) -> tuple[np.ndarray, np.ndarray]:
    with open(input, "r") as f:
        inputs = f.read().split("\n\n")
        numbers = np.fromstring(inputs.pop(0), dtype=int, sep=",")
        boards = np.array(
            [np.fromstring(board, dtype=int, sep=" ").reshape(5, 5) for board in inputs]
        )
    return numbers, boards


def part1(input: str):
    numbers, boards = parse_input(input)
    for round, num in enumerate(numbers):
        boards[boards == num] = -1
        for axis in [1, 2]:
            if np.any(check := np.all(boards == -1, axis=axis)):
                num_of_board = np.where(check)[0]
                board = boards[num_of_board]
                print(f"Winner board is: \n\n{board}\n")
                board[board == -1] = 0
                board.sum()
                print(
                    f"Sum of all unmarked numbers is {board.sum()} \
                        and last number is {num} at the round {round}"
                )
                print(f"And the anwser of part1 is: {board.sum() * num}")
                return


def part2(input: str):
    numbers, boards = parse_input(input)
    for round, num in enumerate(numbers):
        boards[boards == num] = -1
        for axis in [1, 2]:
            if np.any(check := np.all(boards == -1, axis=axis)):
                num_of_board = np.where(check)[0]
                prev_board = boards[num_of_board]
                boards = np.delete(boards, num_of_board, 0)
            if boards.shape[0] == 0:
                prev_board[prev_board == -1] = 0
                print(f"The last win board is \n\n {prev_board}\n")
                print(f"At the round {round} and with number {num}")
                print(f"Th sum of all unmarked mumners is {prev_board.sum()}")
                print(f"The answer of the part2 is: {prev_board.sum()* num}")
                return


if __name__ == "__main__":

    _, _ = get_input(task_dir, 4)
    check_example("example.txt", part1)
    check_example("example.txt", part2)
    part1("input.txt")
    print("\n")
    part2("input.txt")
    generate_readme(task_dir, 4)
