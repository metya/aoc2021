import os, sys
import numpy as np

task_dir = os.path.dirname(__file__)
sys.path.append(f"{task_dir}/..")
from get_tasks import get_input, check_example, generate_readme


def bits2num(bits: np.ndarray) -> int:
    return (bits * 2 ** np.arange(bits.shape[0] - 1, -1, -1)).sum()


def part1(input):

    diagnostics = np.array(
        [list(bits.replace("\n", "")) for bits in input], dtype=np.uint8
    )
    a = diagnostics.sum(axis=0)
    b = diagnostics.shape[0] - a
    gamma = (a > b).astype(np.uint)
    epsilon = 1 - gamma
    gamma_decimal = bits2num(gamma)
    epsilon_decimal = bits2num(epsilon)

    print(
        f"The gamma rate is {gamma_decimal}, and the epsilon rate is {epsilon_decimal}."
    )
    print(
        f"The power comnsuimpsion of the submarine and the answer of part1 is: {gamma_decimal * epsilon_decimal}"
    )


def filter_array(array: np.ndarray, CO2: bool) -> np.ndarray:
    for ind in range(array.shape[1]):
        a = array.sum(axis=0)
        b = array.shape[0] - a
        c = (a >= b).astype(np.uint)
        if CO2:
            c = 1 - c
        if (temp := array[array[:, ind] == c[ind]]).size != 0:
            array = temp
        else:
            break
    return array


def part2(input):

    diagnostics = np.array(
        [list(bits.replace("\n", "")) for bits in input], dtype=np.uint8
    )
    O2 = filter_array(diagnostics, False)
    CO2 = filter_array(diagnostics, True)
    O2_decimal = bits2num(O2[0])
    CO2_decimal = bits2num(CO2[0])
    print(f"The oxygen generator rating is {O2_decimal}")
    print(f"The CO2 scrubber rating is  {CO2_decimal}")
    print(
        f"The life support raiting and the answer of part2 is: {O2_decimal*CO2_decimal}"
    )


if __name__ == "__main__":
    import timeit

    input, example = get_input(task_dir, 3)
    setup = """
    
from __main__ import part1, part2
import os, sys
import numpy as np
task_dir = os.path.dirname(__file__)
sys.path.append(f"{task_dir}/..")
from get_tasks import get_input
input, example = get_input(task_dir, 3)
    """

    check_example(example, part1)
    check_example(example, part2)
    part1(input)
    print("\n")
    part2(input)
    # meas = timeit.timeit("part2(input)", setup=setup, number=100)
    # print((meas))

    generate_readme(task_dir, 3)
