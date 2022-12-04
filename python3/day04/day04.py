
def read_lines(path):
    lines = None
    with open(path) as file:
        lines = [line.rstrip() for line in file]
    return lines


def lines_to_ranges(lines):
    pairs = [x.split(',') for x in lines]
    pairs = [[x[0].split('-'), x[1].split('-')] for x in pairs]
    intpairs = [[[int(x) for x in y] for y in item ] for item in pairs]
    rgs = [ [range(y[0], y[1] + 1 ) for y in x] for x in intpairs]
    # sets = [[set(y) for y in x] for x in rgs]
    return rgs


def count_overlaps(rangepairs):
    i = 0
    o = 0
    for rp in rangepairs:
        r1, r2 = rp
        s1, s2 = [set(x) for x in rp]
        if s1.issubset(s2):
            print(f"Range {r1} is subset of {r2}")
            i += 1
        elif s1.issuperset(s2):
            print(f"Range {r1} is SUPERSET of {r2}")
            i += 1
        if len(s1.intersection(s2)) > 0:
            o += 1
    print(f"Total lines\t {len(rangepairs)}")
    print(f"Total contains\t {i}")
    print(f"Total overlaps\t {o}")

def main():
    print(f"done with main")
    lines = read_lines('day04/input.txt')
    ranges = lines_to_ranges(lines)
    # print(ranges)
    count_overlaps(ranges)
    


main()

