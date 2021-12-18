from doctest import Example
import os, sys, re
task_dir = os.path.dirname(__file__)
sys.path.append(f'{task_dir}/..')
from get_tasks import get_input, generate_readme, check_example

def hit(position, target):
    x, y = position
    x1, x2, y1, y2 = target
    return True if x <= x2 and x >= x1 and y >= y1 and y <= y2 else False

def launch_prob(target):
    succes = {}
    succes_init_velocity = []
    for i in range(1, target[1]+1):
        for j in range(target[2], -target[2]):
            init_velocity = i, j
            hor, ver = i, j
            hy = 0
            x, y  = 0, 0
            while not (apple := hit((x, y), target)):
                py = y
                x += hor; y += ver
                if py > y and hy == 0: hy = py
                if hor < 0: hor += 1
                elif hor > 0: hor -= 1
                else: pass
                ver -= 1
                if (x > target[1]) or (y < target[2]): break
            if apple: 
                succes[hy] = init_velocity
                succes_init_velocity.append(init_velocity)
    return succes, succes_init_velocity

def part1(input: list[str]):
    target = [int(c) for c in re.findall('-?\d+', input[0])]
    hy, _ = launch_prob(target)
    print("The answer of part1 is:", max(hy))
    
def part2(input: list[str]):
    target = [int(c) for c in re.findall('-?\d+', input[0])]
    _, v = launch_prob(target)
    print("The answer of part1 is:", len(v))
    
    
if __name__ == "__main__":
    input, example = get_input(task_dir, 17)
    
    check_example(example, part1)
    check_example(example, part2)
    
    part1(input)
    part2(input)
    
    generate_readme(task_dir, 17)