import os, sys

task_dir = os.path.dirname(__file__)
sys.path.append(f"{task_dir}/..")
import numpy as np
from get_tasks import get_input, generate_readme, check_example, bench
from itertools import takewhile
from scipy import ndimage


def parse(input, test=False):
    if test:
        code = (
            "".join([line for line in takewhile(lambda l: len(l) > 0, input)])
            .replace("#", "1")
            .replace(".", "0")
        )
        image = np.array([list(line) for line in input[8:]])
    else:
        code = input[0].replace("#", "1").replace(".", "0")
        image = np.array([list(line) for line in input[2:]])
    image[image == "."] = 0
    image[image == "#"] = 1
    return image.astype(int), code


def naive_enhance_image(image, code, step):
    if code[0] == "0":
        pad = 0
        val = pad
    else:
        pad = step % 2
        val = 1 - pad
    sp = 3 if step == 0 else 1
    enhance_image = np.pad(image, sp, "constant", constant_values=pad)
    enhanced_image = np.full_like(enhance_image, val, dtype=int)
    for i in range(enhance_image.shape[0] - 2):
        for j in range(enhance_image.shape[1] - 2):
            win = enhance_image[i : i + 3, j : j + 3]
            enhanced_image[i + 1, j + 1] = code[
                int("".join(win.flatten().astype(str)), 2)
            ]
    return enhanced_image


# works ony in test
def scipy_enhance_image(image, code, outside=0):
    def convert(values):
        string = "".join(str(int(value)) for value in values)
        return code[int(string, 2)]

    enhance_image = np.pad(image, 1)
    ndimage.generic_filter(
        enhance_image, convert, size=3, mode="constant", cval=outside
    )


def part1(input, test=False):
    image, code = parse(input, test)
    for step in range(2):
        image = naive_enhance_image(image, code, step)
    print("The answer of part1 is:", image.sum())


@bench
def part2(input, test=False):
    image, code = parse(input, test)
    for step in range(50):
        image = naive_enhance_image(image, code, step)
    print("The answer of part2 is:", image.sum())


if __name__ == "__main__":
    input, example = get_input(task_dir, 20)

    part1(example, True)
    part2(example, True)

    part1(input)
    part2(input)

    generate_readme(task_dir, 20)
