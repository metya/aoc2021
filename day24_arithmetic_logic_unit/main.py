import os, sys, re
task_dir = os.path.dirname(__file__)
sys.path.append(f'{task_dir}/..')
from get_tasks import get_input, generate_readme, check_example


def ALU(program, number):
    number = iter(map(int, str(number)))
    ma = {'w':0, 'z':0, 'x':0, 'y':0}
    for idx, line in enumerate(program):
        if len(inp := line.split()) == 2: ma[inp[1]] = next(number)
        else:
            ins, a, b = line.split()
            if ins == 'add': ma[a] = ma[a] + int(b) if b.isdigit() or b.startswith('-') else ma[a] + ma[b]
            if ins == 'mul': ma[a] = ma[a] * int(b) if b.isdigit() or b.startswith('-') else ma[a] * ma[b]
            if ins == 'mod': 
                if ma[a] < 0 : raise ValueError(f'{a} < 0! or {b} <= 0: {ma[a]}. istruction number {idx}: {line}')
                else: ma[a] = ma[a] % int(b) if b.isdigit() else ma[a] % ma[b]
            if ins == 'div': 
                if (b.isdigit() and int(b) < 0) or (not b.isdigit() and ma[b] < 0): 
                    raise ValueError(f'{b} <= 0: {b if b.isdigit() else ma[b]}. istruction number {idx}: {line}')
                else: ma[a] = int(ma[a] / int(b)) if b.isdigit() or b.startswith('-') else int((ma[a] / ma[b]))
            if ins == 'eql': 
                if b.isdigit() and ma[a] == int(b):
                    ma[a] = 1 
                elif not b.isdigit() and ma[b] == ma[a]:
                    ma[a] = 1
                else:
                    ma[a] = 0
    return ma['w'], ma['x'], ma['y'], ma['z']

def get_equations_from_input(input):
    placeholder = 'abcdefghijklmn'
    number = iter(placeholder)
    pstack = []
    diffs = []
    stack = []
    equations = []
    for idx, line in enumerate(input):
        match idx % 18:
            case 5 | 15: diffs.append(line)
    for idx, line in enumerate(diffs):
        _, a, b = line.split()
        if a == 'x' and b.startswith("-"):
            pstack.append(['pop', f'{b} = {next(number)}'])
        elif a == 'x':
            pstack.append(['push', f'{next(number)} + {diffs[idx+1].split()[2]}'])
    for line in pstack:
        if line[0] == 'push':
            stack.append(line[1])
        elif line[0] == 'pop':
            pop = stack.pop().split('+')
            val = line[1].split('=')
            equations.append([f"{pop[0]} + {eval(pop[-1]+val[0])} = {val[-1]}"])
    return equations

def part1(equations):
    placeholder = 'abcdefghijklmn'
    for equation in equations:
        if re.findall(r"\-", equation[0]):
            equation = equation[0]
            letter1 = equation[0]
            letter2 = equation[-1]
            placeholder = placeholder.replace(letter1, '9')
            equation = equation.replace(letter1, '9')
            placeholder = placeholder.replace(letter2, str(eval(equation.split('=')[0])))
        else:
            equation = equation[0][::-1]
            letter1 = equation[0]
            letter2 = equation[-1]
            placeholder = placeholder.replace(letter1, '9')
            equation = equation.replace(letter1, '9')
            placeholder = placeholder.replace(letter2, str(9 - int(equation.split('=')[1].split('+')[0]))) 
    print("The answer of part1 is:", placeholder)
    return placeholder

def part2(equations):
    placeholder = 'abcdefghijklmn'
    for equation in equations:
        if re.findall(r"\-", equation[0]):
           equation = equation[0][::-1]
           letter1 = equation[0]
           letter2 = equation[-1]
           placeholder = placeholder.replace(letter1, '1')
           equation = equation.replace(letter1, '1')
           placeholder = placeholder.replace(letter2, str(1 + int(equation.split('=')[1].split('+')[0][1]))) 
        else:
            equation = equation[0]
            letter1 = equation[0]
            letter2 = equation[-1]
            placeholder = placeholder.replace(letter1, '1')
            equation = equation.replace(letter1, '1')
            placeholder = placeholder.replace(letter2, str(eval(equation.split('=')[0])))
    print("The answer of part2 is:", placeholder)
    return placeholder
            
            
if __name__ == '__main__':

    input, example = get_input(task_dir, 24)
    
    equations = get_equations_from_input(input)
    
    part1(equations)
    part2(equations)

    generate_readme(task_dir, 24)

    