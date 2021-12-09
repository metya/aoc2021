import os, sys
task_dir = os.path.dirname(__file__)
sys.path.append(f'{task_dir}/..')
from get_tasks import get_input, check_example, generate_readme

def part1(input: list[str]):
    count = 0
    for line in input:
        line = line.split()[11:]
        for comb in line:
            match len(comb): 
                case 2 | 3 | 4 | 7: count += 1
    print('The answer of part1 is:', count)
    
def part2(input: list[str]):
    numbers = []
    for lines in input:
        six, five = [], []
        for comb in lines.split()[:10]:
            match len(comb): 
                case 2: one = set(comb)
                case 3: seven = set(comb)
                case 4: four = set(comb)
                case 7: eight = set(comb)
                case 6: six.append(set(comb))
                case 5: five.append(set(comb))
        three = [i for i in five if len(i - one) == 3].pop()
        five.pop(five.index(three))
        a = (seven - one)
        g = three - four - seven
        b = four - three
        e = eight - four - a - g
        d = eight - a - b - e - g - one
        if (five[0] - three) == b: 
            f = five[0] & one
            c = one - f
        else:
            c = five[0] & one
            f = one - c
        two = a | c | d | e | g
        five = a | d | f | g | b 
        six = a | b | d | e | f | g
        nine = a | b | c | d | f | g
        zero = eight - d
        num = ""
        for comb in lines.split()[11:]:
            if (val := set(comb)) == zero : num += '0'
            elif val == one: num += '1'
            elif val == two: num += '2'
            elif val == three: num += '3'
            elif val == four: num += '4'
            elif val == five: num += '5'
            elif val == six: num += '6'
            elif val == seven: num += '7'
            elif val == eight: num += '8'
            elif val == nine: num += '9'
            else : raise Exception("There is no such code")
        numbers.append(int(num))
    
    print('The answer of part2 is:', sum(numbers))
    
if __name__ == "__main__":
    input, example = get_input(task_dir, 8)
    
    check_example(example, part1)
    check_example(example, part2)
    part1(input)
    part2(input)
    
    generate_readme(task_dir, 8)
    
