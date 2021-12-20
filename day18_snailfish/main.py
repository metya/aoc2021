import os, sys, re

task_dir = os.path.dirname(__file__)
sys.path.append(f"{task_dir}/..")
from get_tasks import get_input, generate_readme, check_example, bench
from math import floor, ceil


def explodes(strl, v=False):
    for pair in re.finditer(r"\[(\d+),(\d+)\]", strl):
        sd, ed = pair.start(), pair.end()
        if strl[:sd].count("[") - strl[:sd].count("]") >= 4:
            p1, p2 = int(pair.group(1)), int(pair.group(2))
            numreplace = list(re.finditer(r"\d+", strl[:sd]))[::-1]
            if numreplace:
                s, e, v = (
                    numreplace[0].start(),
                    numreplace[0].end(),
                    int(numreplace[0][0]),
                )
                before = strl[:s] + str(p1 + v) + strl[e:sd]
            else:
                before = strl[:sd]
            numreplace = list(re.finditer(r"\d+", strl[ed:]))
            if numreplace:
                s, e, v = (
                    numreplace[0].start(),
                    numreplace[0].end(),
                    int(numreplace[0][0]),
                )
                after = strl[ed : ed + s] + str(p2 + v) + strl[ed + e :]
            else:
                after = strl[ed:]
            return before + "0" + after, True
    return strl, False


def split(strl):
    for num in re.finditer(r"\d{2}", strl):
        s, e = num.start(), num.end()
        d = int(num[0])
        ls = floor(d / 2)
        rs = ceil(d / 2)
        return strl[:s] + f"[{ls},{rs}]" + strl[e:], True
    return strl, False


def addition(l):
    e = True
    while e:
        l, e = explodes(l)
        if not e:
            l, e = split(l)
    return l


def magnitude(line):
    while pairs := list(re.finditer(r"\[(\d+),(\d+)\]", line)):
        for pair in pairs[::-1]:
            sd, ed = pair.start(), pair.end()
            p1, p2 = int(pair[1]), int(pair[2])
            line = line[:sd] + str(p1 * 3 + p2 * 2) + line[ed:]
    return int(line)

@bench
def part1(input):
    res = []
    for line in input:
        res.append(line)
        if len(res) > 1:
            res.append(addition(f"[{res.pop(0)},{res.pop(0)}]"))
    print(magnitude(res[0]))

@bench
def part2(input):
    mag = []
    for ind, line in enumerate(input):
        for ind2, line2 in enumerate(input):
            if ind == ind2:
                continue
            mag.append(magnitude(addition(f"[{line},{line2}]")))
    print(max(mag))


if __name__ == "__main__":
    input, example = get_input(task_dir, 18)

    part1(input)
    part2(input)

    generate_readme(task_dir, 18)