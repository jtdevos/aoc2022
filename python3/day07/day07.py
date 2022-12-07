def read_lines(path):
    lines = None
    with open(path) as file:
        lines = [line.rstrip() for line in file]
    return lines



def main():
    lines = read_lines('day07/input.txt')
    print(f"Read file:: total lines:{len(lines)}")

main()
