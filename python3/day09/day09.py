import os, math
def cls():
    os.system('cls||clear')

def clamp(n, smallest, largest): 
    return max(smallest, min(n, largest))

def clamp_tuple(pt):
    return (
        clamp(pt[0], -1, 1),
        clamp(pt[1], -1, 1)
    )

def clamp_point(pt):
    return Point(clamp(pt.x, -1, 1), clamp(pt.y, -1, 1))

def read_lines(path):
    lines = None
    with open(path) as file:
        lines = [line.rstrip() for line in file]
    return lines

class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.pos_history = list()
        self.move(0,0) #log first position
    
    def pos(self):
        """return position as tuple"""
        return (self.x, self.y)
    
    def move(self, x, y):
        self.x += x
        self.y += y
        self.pos_history.append(self.pos())
    
    def diff(self, p):
        """subtract p from this point, return (x,y) tuple"""
        d = Point(self.x - p.x, self.y - p.y)
        return d
    
    def dist(self):
        """treating a point as a vector, return distance"""
        return math.sqrt(self.x**2 + self.y**2)
    
    def clamp(self):
        """return clamped copy of this vector """
        return clamp_point(self)
    
    def __str__(self):
        return f"Point({self.x}, {self.y})"

def dist(i, j):
    return math.sqrt(i**2 + j**2)

def read_lines(path):
    lines = None
    with open(path) as file:
        lines = [line.rstrip() for line in file]
    return lines   

def parse_commands(path):
    lines = read_lines(path)
    commands = [line.split(' ') for line in lines]
    commands = [[c[0], int(c[1])] for c in commands]
    return commands
    

def test1():
    pts = []
    for x in range(-10, 10):
        for y in range(-10, 10):
            p = (x,y)
            print(f'orig:{p}\t clamp:{clamp_tuple(p)}')

def code_to_vector(code):
    dct = {
        'U': (0,1),
        'R': (1, 0),
        'D': (0, -1),
        'L': (-1, 0)}
    v = dct[code]
    return v


def test2(): 
    """testing out points """
    ph = Point()
    pt = Point()
    ph.move(1,1)
    ph.move(-1,1)
    print(f'Point ph: {ph.pos()}')
    print(f'Point ph history: {ph.pos_history}')
    
def part1(commands):
    ph = Point()
    pt = Point()
    for code, rpt in commands:
         v = code_to_vector(code)
         print(f"Command:{code}->{v}\t times:{rpt}")
         # move in specified direction rpt times
         for i in range(rpt):
            ph.move(v[0], v[1])
            print(f"  ph:{ph}\t pt:{pt}\t dist:{ph.diff(pt).dist()}")
            if(ph.diff(pt).dist()) >= 2:
                print(f"    Distance too great -- scooting tail")
                scootVec = ph.diff(pt).clamp()
                pt.move(scootVec.x, scootVec.y)
                print(f"    New tail position:{pt} (distance:{ph.diff(pt).dist()})")
    print("*"*20)
    print(f"Tail history:\t {pt.pos_history}")
    tc = set(pt.pos_history)

    print(f"Tail coverage:\t {tc}")
    print(f"count of spaces covered: {len(tc)}")


def run_commands(commands, chainsize):
    pchain = [Point() for _ in range(chainsize)]
    ph = pchain[0]
    pt = pchain[-1]
    for code, rpt in commands:
         v = code_to_vector(code)
         print(f"Command:{code}->{v}\t times:{rpt}")
         # move in specified direction rpt times
         for _ in range(rpt):
            # move the absolute head, then determine if we need to move subsequent tails
            ph.move(v[0], v[1])
            for i in range(1, chainsize):
                tph = pchain[i-1]
                tpt = pchain[i]
                print(f"  segment[{i-1}]:{tph}\t segment[{i}]:{tpt}\t dist:{tph.diff(tpt).dist()}")
                if(tph.diff(tpt).dist()) >= 2:
                    print(f"    Distance too great -- scooting tail")
                    scootVec = tph.diff(tpt).clamp()
                    tpt.move(scootVec.x, scootVec.y)
                    print(f"    New tail position:{tpt} (distance:{tph.diff(tpt).dist()})")
    print("*"*20)
    print(f"Tail history:\t {pt.pos_history}")
    tc = set(pt.pos_history)

    print(f"Tail coverage:\t {tc}")
    print(f"count of spaces covered: {len(tc)}")



                




def main(path):
    cmds = parse_commands(path)
    print(cmds)
    # part 1
    run_commands(cmds, 2)
    # part 2
    run_commands(cmds, 10)


# main('day09/sample.txt')
main('day09/input.txt')
