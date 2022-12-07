

def part1():
    with open("adventofcode/day6/input.txt") as f:
        input = f.readline()
    print(find_first_non_repeating(input, 4))


def part2():
    with open("adventofcode/day6/input.txt") as f:
        input = f.readline()
    print(find_first_non_repeating(input, 14))


def find_first_non_repeating(input: str, sequence_size: int):
    seen = set([])
    offset = sequence_size - 1
    for i in range(offset,len(input)):
        if len(set(input[i-offset:i+1])) == sequence_size:
            return (i+1)

if __name__ == '__main__':
    part1()
    part2()