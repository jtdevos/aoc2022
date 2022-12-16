import os, math, re
from collections import namedtuple
Point = namedtuple('Point', 'x y')

def debug(msg):
    # pass
    print(msg)

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

def manhat_dist(p1:Point, p2:Point):
    dist = abs(p2.x - p1.x) + abs(p2.y - p1.y)
    # debug(f'{p1=}, {p2=}, dist:{dist}')
    return dist

def part1(pairs, testRow):
    xmin = min([beacon.x for (_, beacon) in pairs])
    xmax = max([beacon.x for (_, beacon) in pairs])
    debug("\n\n Distances::")
    debug(f"{xmin=}, {xmax=}")
    safesquares = 0
    #find
    dists = [(sensor, manhat_dist(sensor, beacon)) for (sensor, beacon) in pairs]
    for s, d in dists:
        print(f"{s=}, {d=}")
    for x in range(xmin, xmax+1):
        print(f"{x=}")
        safe = True
        tp = Point(x, testRow)
        for sensor, dist in dists:
            print(f"{sensor=},{tp=}:: {manhat_dist(tp, sensor)} > {dist=} = {manhat_dist(tp, sensor)> dist}")
            if manhat_dist(tp, sensor) > dist:
                safe =  safe & False
        if safe:
            safesquares += 1
            print(f"space {tp=} is safe")
        print("--------")
            


        #for each x position in row y:
            # is (x,y) close/closer than alll sensor -> beacon combos? add to count.

def processPair(line):
    groups = REGEX.match(line).groups()
    nums = [int(x) for x in groups]
    sensor = Point(nums[0], nums[1])
    beacon = Point(nums[2], nums[3])
    pair = (sensor, beacon)
    debug(f"{pair=}")
    return pair 

def main(path):
    pairs = read_lines(path, processPair)
    part1(pairs, testRow=10)

main('day15/sample.txt')