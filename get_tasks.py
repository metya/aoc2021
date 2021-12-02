import requests
import os


def get_input(task_dir, day):
    input_path = os.path.join(task_dir, "input.txt")
    example_path = os.path.join(task_dir, "example.txt")

    cookies_dict = {
        "session": "53616c7465645f5ffe3db8d154199da4d6e4e569142fda21d3350f5e550f2a4c509bd1b147264ffe0a0d2124909ec5d6"
    }

    if os.path.exists(input_path):
        with open(input_path, "r") as f:
            input = f.readlines()
    else:
        input = requests.get(
            f"https://adventofcode.com/2021/day/{day}/input", cookies=cookies_dict
        ).text
        with open(input_path, "w") as f:
            f.write(input)
        input = input.splitlines()
    if os.path.exists(example_path):
        with open(example_path, "r") as e:
            example = e.readlines()
    else:
        example = None

    return input, example


if __name__ == "__main__":
    print(get_input("day_1_sonar_sweep", 1))
