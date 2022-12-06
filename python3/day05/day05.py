import re

def read_lines(path):
    lines = None
    with open(path) as file:
        lines = [line.rstrip() for line in file]
    return lines


def init_stacks(lines):
    # get line w/ stack numbers
    numsline = next(filter(lambda line: '1' in line, lines), None)
    maxidx = 0
    for char in numsline:
        if char.isnumeric():
            maxidx = int(char) if int(char) > maxidx else maxidx    
    # print( f'numsline is: {numsline}, maxidx is {maxidx}')
    stacks = []
    for i in range(maxidx):
        stacks.append(list())
    return stacks

def load_stacks(lines):
    #keep going until you get a line of 
    stacks = init_stacks(lines)
    stacklines = [x for x in lines if '[' in x]
    # print(f'read all stacklines. size {len(stacklines)}')
    for i, line in enumerate(stacklines):
        # print(f"line {i}: {line}")
        for j, char in enumerate(line):
            if char.isalpha():
                idx = int((j-1)/4)
                # print(f"is alpha character: {char}:{idx}")
                stacks[idx].insert(0, char)
    return stacks

def load_instructions(lines):
    inst_lines = [line for line in lines if 'move' in line]
    # exp = re.compile(r"move (\d+) from (\d+) to (\d+)")
    exp = re.compile(r"\d+")
    instructions = [[int(x) for x in exp.findall(line)] for line in inst_lines]
    print("Instructions: ")
    # for (qty, src, dest) in instructions:
    #     print(f"from:{src}\t to:{dest}\t qty:{qty}")
    return instructions
    
def stack_report(stacks):
    print("Stack Report")
    for i, stack in enumerate(stacks):
        print(f'\t stack {i}:\t {stack}')
    print(f"Top of stacks: {''.join([x[len(x)-1] for x in stacks])}")

def update_stacks(stacks, src, dest, qty):
    for i in range(qty):
        stacks[dest].append(stacks[src].pop())

def update_stacks_9001(stacks, src, dest, qty):
    items = stacks[src][0-qty:]
    del stacks[src][0-qty:]
    stacks[dest].extend(items)
    
def part1(stacks, instructions):
    for qty, src, dest in instructions:
        update_stacks(stacks, src-1, dest-1, qty)

def part2(stacks, instructions):
    for qty, src, dest in instructions:
        update_stacks_9001(stacks, src-1, dest-1, qty)

def main():
    lines = read_lines('day05/input.txt')
    print(f"lines loaded. size: {len(lines)}")
    stacks = load_stacks(lines)
    instructions = load_instructions(lines)
    print("Before")
    stack_report(stacks)

    part1(stacks, instructions)
    print("\nAfter Stacker 9000")
    stack_report(stacks)

    stacks = load_stacks(lines)
    part2(stacks, instructions)
    print("\nAfter Stacker 9001")
    stack_report(stacks)
    





main()