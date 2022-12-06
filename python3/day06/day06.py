def read_lines(path):
    lines = None
    with open(path) as file:
        lines = [line.rstrip() for line in file]
    return lines

def unique_finder(data, size):
    idx = -1
    for i in range(size - 1, len(data)):
        subset = data[i-size:i]
        ds = set(list(subset))
        if len(ds) == size:
            print(f"found unique header - idx:{i}\t data:{subset}")
            idx = i
            break

def part1(data):
    unique_finder(data, 4)

def part2(data):
    unique_finder(data, 14)

def main():
    lines = read_lines('day06/input.txt')
    data = lines[0]
    print('read all data')
    print(f'lines: {len(lines)}')
    print(f'data lenth: {len(data)}')
    part1(data)
    part2(data)

main()