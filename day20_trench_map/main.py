import os, sys

task_dir = os.path.dirname(__file__)
sys.path.append(f"{task_dir}/..")
import numpy as np
from get_tasks import get_input, generate_readme, check_example, bench
from itertools import takewhile
from scipy.signal import convolve2d
from numpy.lib.stride_tricks import sliding_window_view


def parse(input, test=False):
    if test:
        code = (
            "".join([line for line in takewhile(lambda l: len(l) > 0, input)])
            .replace("#", "1")
            .replace(".", "0")
        )
        code = np.array(list(code), dtype=int)
        image = np.array([list(line) for line in input[8:]])
    else:
        code = np.array(list(input[0].replace("#", "1").replace(".", "0")), dtype=int)
        image = np.array([list(line) for line in input[2:]])
    image[image == "."] = 0
    image[image == "#"] = 1
    return image.astype(int), code


def naive_virgin_enhance_image(image, code, steps):
    for step in range(steps):
        match code[0]:
            case 0: pad = 0; val = 0
            case _: pad = step % 2; val = 1 - pad
        sp = 3 if step == 0 else 1
        enhance_image = np.pad(image, sp, constant_values=pad)
        enhanced_image = np.full_like(enhance_image, val, dtype=int)
        for i in range(enhance_image.shape[0] - 2):
            for j in range(enhance_image.shape[1] - 2):
                win = enhance_image[i : i + 3, j : j + 3]
                enhanced_image[i + 1, j + 1] = code[
                    win.flatten()[0] * 256 + np.packbits(win.flatten()[1:])
                ]
        image = enhanced_image
    return image


def true_vectorized_chad_enhance_image(image, code, steps, outside=0, pad_size=2):
    for _ in range(steps):
        image = np.pad(image, pad_size, constant_values=outside)

        windows = sliding_window_view(image, (3, 3))
        windows = windows.reshape(*windows.shape[:2], 9)
        codes = windows[:, :, 0] * 256 + np.packbits(windows[:, :, 1:]).reshape(
            windows.shape[:2]
        )
        image = code[codes]
        outside = code[outside * 511]
    return image


def literally_genious_conv_enhance_image(image, code, steps, outside=0):
    kernel = np.array(
    [
        [ 1,  2,  4],
        [ 8, 16, 32],
        [64,128,256]
    ]
)   
    for _ in range(steps):
        image = code[convolve2d(image, kernel, fillvalue=outside)]
        outside = code[outside*511]
    return image

@bench
def part1(input, test=False, method='conv_kernel'):
    image, code = parse(input, test)
    if method == 'conv_kernel':
        image = literally_genious_conv_enhance_image(image, code, steps=2)
    elif method == 'vectorized':
        image = true_vectorized_chad_enhance_image(image, code, steps=2)
    else: 
        image = naive_virgin_enhance_image(image, code, steps=2)
    print("The answer of part1 is:", image.sum())


@bench
def part2(input, test=False, method='conv_kernel'):
    image, code = parse(input, test)
    if method == 'conv_kernel':
        image = literally_genious_conv_enhance_image(image, code, steps=50)
    elif method == 'vectorized':
        image = true_vectorized_chad_enhance_image(image, code, steps=50)
    else: 
        image = naive_virgin_enhance_image(image, code, steps=50)
    print("The answer of part2 is:", image.sum())


if __name__ == "__main__":
    input, example = get_input(task_dir, 20)

    part1(example, True)
    part2(example, True)

    part1(input, method='conv_kernel')
    part2(input, method='conv_kernel')

    generate_readme(task_dir, 20)
