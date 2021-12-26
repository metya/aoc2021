import os, sys, copy
from attr import field
task_dir = os.path.dirname(__file__)
sys.path.append(f'{task_dir}/..')
import numpy as np
from get_tasks import get_input, generate_readme, check_example, bench

def can_move_any(field, hight, width, count):
    bools = []
    cucumbers = []
    for x in range(hight-1):
        for y in range(width-1):
            if field[x][y]=='>' and field[x][y+1] == '.':
                bools.append(True)
                cucumbers.append([1, x, y])
            if field[x][y]=='>' and field[x][y+1] != '.':
                bools.append(False)
            if field[x][y]=='v' and field[x+1][y] == '.':
                bools.append(True)
                cucumbers.append([2, x, y])
            if field[x][y]=='v' and field[x+1][y] != '.':
                bools.append(False)
            if (y == width-2) and (field[x][y+1] == '>') and (field[x][0] == '.'):
                bools.append(True)
                cucumbers.append([3, x, y+1])
            if (y == width-2) and (field[x][y+1] == '>') and (field[x][0] != '.'):
                bools.append(False)
            if (y == width-2) and (field[x][y+1] == 'v') and (field[x+1][y+1] == '.'):
                bools.append(True)
                cucumbers.append([2, x, y+1])
            if (y == width-2) and (field[x][y+1] == 'v') and (field[x+1][y+1] != '.'):
                bools.append(False)
                
            if (x == hight-2) and (field[x+1][y] == 'v') and (field[0][y] == '.'):
                bools.append(True)
                cucumbers.append([4, x+1, y])
            if (x == hight-2) and (field[x+1][y] == 'v') and (field[0][y] != '.'):
                bools.append(False)
            if (x == hight-2) and (field[x+1][y] == '>') and (field[x+1][y+1] == '.'):
                bools.append(True)
                cucumbers.append([1, x+1, y])
            if (x == hight-2) and (field[x+1][y] == '>') and (field[x+1][y+1] != '.'):
                bools.append(False)
    if field[hight-1][width-1]=='>' and field[hight-1][0]=='.':
        bools.append(True)
        cucumbers.append([3, hight-1, width-1])
    if field[hight-1][width-1]=='>' and field[hight-1][0]!='.':
        bools.append(False)
    if field[hight-1][width-1]=='v' and field[0][width-1]=='.':
        bools.append(True)
        cucumbers.append([4, hight-1, width-1])
    if field[hight-1][width-1]=='v' and field[0][width-1]!='.':
        bools.append(False)
    if len(bools) != count: raise Exception('count != bools!', len(bools))
    return cucumbers


def moving(orig_field, step=None):
    copy_field = copy.deepcopy(orig_field)
    hight, width = len(copy_field), len(copy_field[0])
    count = 0
    for x in range(hight):
        for y in range(width):
            if copy_field[x][y] != '.': count+=1
    steps = 0
    move = True
    while move:
        steps+=1
        for herd in ['east', 'north']:
            cucumbers = can_move_any(copy_field, hight, width, count)
            if len(cucumbers) < 1: move = False
            for cucumber in cucumbers:
                if herd == 'east':
                    match cucumber:
                        case [1, x, y]: copy_field[x][y] = '.'; copy_field[x][y+1]='>'
                        case [3, x, y]: copy_field[x][y] = '.'; copy_field[x][0]='>'
                else:
                    match cucumber:
                        case [2, x, y]: copy_field[x][y] = '.'; copy_field[x+1][y]='v'
                        case [4, x, y]: copy_field[x][y]='.'; copy_field[0][y]='v'
            
        
        if step and steps == step:
            break
    return copy_field, steps, ["".join(line) for line in copy_field]

def check_move(arr):
    right = np.where(arr == '>')
    down = np.where(arr == 'v')
    h, w = arr.shape
    can_move = []
    for x, y in zip(right[0], right[1]):
        if y == w-1:
            if arr[x, 0] == '.': can_move.append([3, x, y])
        else:
            if arr[x, y+1] == '.': can_move.append([1, x, y])
    for x, y in zip(down[0], down[1]):
        if x == h-1:
            if arr[0, y] == '.': can_move.append([4, x, y])
        else:
            if arr[x+1, y] == '.': can_move.append([2, x, y])
    return can_move, True if can_move else False

def array_like(input):
    arr = np.array([list(line) for line in input])
    np.count_nonzero(arr!='.')
    steps = 0
    move = True
    while move:
        steps+=1
        for herd in ['east', 'north']:
            cucumbers, move = check_move(arr)
            if len(cucumbers) < 1: move = False; break
            for cucumber in cucumbers:
                if herd == 'east':
                    match cucumber:
                        case [1, x, y]: arr[x][y] = '.'; arr[x][y+1]='>'
                        case [3, x, y]: arr[x][y] = '.'; arr[x][0]='>'
                else:
                    match cucumber:
                        case [2, x, y]: arr[x][y] = '.'; arr[x+1][y]='v'
                        case [4, x, y]: arr[x][y]='.'; arr[0][y]='v'
    return arr, steps, ["".join(line) for line in arr]


@bench
def part1(input):
    field = [list(line) for line in input]
    _, steps, _ = array_like(field)
    print('The asnwer of part1 is:', steps+1)



if __name__ == '__main__':
    
    input, example = get_input(task_dir, 25)
    
    check_example(example, part1)
    part1(input)
    
    generate_readme(task_dir, 25)