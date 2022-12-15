import os, math, re

def debug(msg):
    pass
    #print(msg)

def cls():
    os.system('cls||clear')

def read_lines(path, processor = None):
    lines = None
    if processor is None:
        processor = lambda x:  x
    with open(path) as file:
        lines = [processor(line.rstrip()) for line in file]
    return lines

# line  should match Sensor at x=2, y=18: closest beacon is at x=-2, y=15
REGEX = re.compile(r'Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)')


def part1():
    pass

def processLine(line):
    groups = REGEX.match(line).groups()
    groups = [int(x) for x in groups]
    print(groups)
    return groups

def main(path):
    lines = read_lines(path, processLine)


main('day15/sample.txt')