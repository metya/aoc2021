import os
import requests
import bs4
import markdownify as md
import time
from typing import Any, Callable


def generate_readme(task_dir: str, day: int):

    readme_path = os.path.join(task_dir, "README.md")
    cookies_dict = {
        "session": "53616c7465645f5ffe3db8d154199da4d6e4e569142fda21d3350f5e550f2a4c509bd1b147264ffe0a0d2124909ec5d6"
    }

    if os.path.exists(readme_path):
        pass
    else:
        soup = bs4.BeautifulSoup(
            requests.get(
                f"https://adventofcode.com/2021/day/{day}", cookies=cookies_dict
            ).content,
            features="html.parser",
        )
        with open(readme_path, "w") as readme:
            readme.write(md.markdownify(str(soup.find_all("article")[0])))
        if len(soup.find_all("article")) > 1:
            with open(readme_path, "a") as readme:
                readme.write(md.markdownify(str(soup.find_all("article")[1])))


def get_input(task_dir: str, day: int) -> tuple[list[str], list[str]]:
    input_path = os.path.join(task_dir, "input.txt")
    example_path = os.path.join(task_dir, "example.txt")

    cookies_dict = {
        "session": "53616c7465645f5ffe3db8d154199da4d6e4e569142fda21d3350f5e550f2a4c509bd1b147264ffe0a0d2124909ec5d6"
    }

    os.makedirs(task_dir, exist_ok=True)

    if os.path.exists(input_path):
        with open(input_path, "r") as f:
            input = f.read().splitlines()
    else:
        input = requests.get(
            f"https://adventofcode.com/2021/day/{day}/input", cookies=cookies_dict
        ).text
        with open(input_path, "w") as f:
            f.write(input)
        input = input.splitlines()

    if os.path.exists(example_path):
        with open(example_path, "r") as e:
            example = e.read().splitlines()
    else:
        example = bs4.BeautifulSoup(
            requests.get(
                f"https://adventofcode.com/2021/day/{day}", cookies=cookies_dict
            ).content,
            features="html.parser",
        ).code.text

        with open(example_path, "w") as f:
            f.write(example)
        example = example.splitlines()

    return input, example


def bench(part):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        value = part(*args, **kwargs)
        print(f"\tevaluation time: {time.perf_counter() - start} s")
        return value

    return wrapper


def check_example(example: Any, part: Callable):
    print(f'\n{10*"-"}Example test here{10*"-"}\n')
    part(example)
    print(f'\n{10*"-"}End example test{10*"-"}\n')


if __name__ == "__main__":
    # print(get_input("day_1_sonar_sweep", 3))
    generate_readme("../day3_binary_diagnostic", 3)
