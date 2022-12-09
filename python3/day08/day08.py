def read_lines(path):
    lines = None
    with open(path) as file:
        lines = [line.rstrip() for line in file]
    return lines

def parse_lines(path):
    """
    Read lines and convert to a 2D array (list of lists)
    """
    lines = read_lines(path)
    grid = [[int(ch) for ch in list(line)] for line in lines]
    w = len(grid[0])
    h = len(grid)
    print(f'Grid parsed. Width:{w}\t Height:{h}')
    return grid

def visibleFromLeftRight(grid, seenTrees):
    w = len(grid[0])
    h = len(grid)
    for row in range(1, h-1):
        mth = grid[row][0]
        print(f"row:{row} mth:{mth} scanning to right -->")
        # scanning left to right
        for col in range(1, w-1):
            th = grid[row][col]
            if th>mth:
                seenTrees.add((row, col))
                mth = th
        # scanning right to left
        mth = grid[row][w-1]
        print(f"row:{row} mth:{mth} scanning to left  <--")
        for col in range(w-2, 0, -1):
            th = grid[row][col]
            if th>mth:
                seenTrees.add((row, col))
                mth = th
        print(f"row:{row} seen trees:{len(seenTrees)}")

def visibleFromUpDown(grid, seenTrees):
    w = len(grid[0])
    h = len(grid)
    for col in range(1, w-1):
        # scan top down 
        mth = grid[0][col]
        print(f"col:{col} mth:{mth} scanning topdown v")
        for row in range(1, h-1):
            th = grid[row][col]
            if th>mth:
                seenTrees.add((row, col))
                mth = th
        # scan down up
        mth = grid[h-1][col]
        print(f"col:{col} mth:{mth} scanning down-up ^")
        for row in range(h-2, 0, -1):
            th = grid[row][col]
            if th>mth:
                seenTrees.add((row, col))
                mth = th
        print(f"col:{col} seen trees:{len(seenTrees)}")


def scenicScore(grid, row, col):
    w = len(grid[0])
    h = len(grid)    
    th = grid[row][col]

    # look up
    scoreUp = 0
    for r in range(row-1, -1, -1):
        cth = grid[r][col]
        scoreUp += 1
        # print(f"({r}, {col}):{cth}  th:{th}")
        if cth >= th:
            break
    
    # look left
    scoreLeft = 0
    for c in range(col-1, -1, -1):
        cth = grid[row][c]
        scoreLeft += 1
        # print(f"({row}, {c}):{cth}  th:{th}")
        if cth >= th:
            break

    # Look right
    scoreRight = 0
    for c in range(col+1, w):
        cth = grid[row][c]
        scoreRight += 1
        # print(f"({row}, {c}):{cth}  th:{th}")
        if cth >= th:
            break

    # Look down
    scoreDown = 0
    for r in range(row+1, h):
        cth = grid[r][col]
        scoreDown += 1
        # print(f"({r}, {col}):{cth}  th:{th}")
        if cth >= th:
            break
    sc = scoreDown * scoreUp * scoreLeft * scoreRight
    print(f"score up:   {scoreUp}")
    print(f"score left: {scoreLeft}")
    print(f"score right:{scoreRight}")
    print(f"score down: {scoreDown}")
    print(f"scenic score for ({row}, {col}): {sc} ")
    return sc


    

def part1(grid):
    w = len(grid[0])
    h = len(grid)    
    seenTrees = set()
    visibleFromLeftRight(grid, seenTrees)
    visibleFromUpDown(grid, seenTrees)
    outerTrees = 2*w + 2*h - 4
    innerTrees = len(seenTrees)
    totalVisible = outerTrees + innerTrees
    print(f'Tree count:: inner:{innerTrees}\t outer:{outerTrees} \ttotal:{totalVisible}')

def part2(grid):
    w = len(grid[0])
    h = len(grid)
    hiscore = 0
    for row in range(1, h-1):
        for col in range(1, w-1):
            s = scenicScore(grid, row, col)
            if s > hiscore:
                hiscore = s
    
    print(f"Highest score: {hiscore}")










def main(inputfile):
    grid = parse_lines(inputfile)
    # part1(grid)
    part2(grid)


# main('day08/sample.txt')
main('day08/input.txt')