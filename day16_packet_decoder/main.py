import os, sys

task_dir = os.path.dirname(__file__)
sys.path.append(f"{task_dir}/..")
from math import prod
from get_tasks import get_input, generate_readme, check_example



def read_litval():
    global cur
    blitval = ""
    while b[cur : cur + 1] == "1":
        cur += 1
        blitval += b[cur : cur + 4]
        cur += 4
    cur += 1
    blitval += b[cur : cur + 4]
    cur += 4
    litval = int(blitval, 2)
    return litval


def read_header():
    global typeID, packver, cur
    packver = int(b[cur : cur + 3], 2)
    cur += 3
    typeID = int(b[cur : cur + 3], 2)
    cur += 3

def read_op():
    global cur
    litsub = []
    if b[cur] == "0":
        cur += 1
        nbits = int(b[cur : cur + 15], 2)
        cur += 15
        end_subpackets = cur + nbits
        while cur != end_subpackets:
            litsub += [parse_block()]
        return litsub
    else:
        cur += 1
        npacks = int(b[cur : cur + 11], 2)
        cur += 11
        n = 0
        while n != npacks:
            n += 1
            litsub += [parse_block()]
        return litsub

def parse_block():
    global typeID, cur, sumpackver, sumval
    read_header()
    sumpackver += packver
    match typeID:
        case 4: return read_litval()
        case 0: return sum(read_op())
        case 1: return prod(read_op())
        case 2: return min(read_op())
        case 3: return max(read_op())
        case 5: subs = read_op(); return 1 if subs[0] > subs[1] else 0
        case 6: subs = read_op(); return 1 if subs[0] < subs[1] else 0
        case 7: subs = read_op(); return 1 if subs[0] == subs[1] else 0

def part1(input, verbose=True):
    global b, cur, sumpackver
    cur = 0
    sumpackver = 0
    packet = input[0]
    b = bin(int(packet, 16))[2:].zfill(len(packet)*4)
    parse_block()
    if verbose:
        print("The answer of part1 is:", sumpackver)
    
def part2(input, verbose=True):
    global b, cur, sumpackver
    cur = 0
    sumpackver = 0
    packet = input[0]
    b = bin(int(packet, 16))[2:].zfill(len(packet)*4)
    val = parse_block()
    if verbose:
        print("The answer of part1 is:", val)

if __name__ == "__main__":
    
    input, example = get_input(task_dir, 16)

    print("PART1")
    for packet in example[3:7]:
        check_example([packet], part1)
    print("PART2")
    for packet in example[7:]:
        check_example([packet], part2)
    
    part1(input)
    part2(input)
    
    generate_readme(task_dir, 16)
