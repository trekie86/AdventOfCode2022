

def part1():
    with open("adventofcode/day6/input.txt") as f:
        input = f.readline()

    seen = set([])
    for i in range(3,len(input)):
        if len(set(input[i-3:i+1])) == 4:
            print(i+1)
            break



def part2():
    with open("adventofcode/day6/input.txt") as f:
        input = f.readline()

    seen = set([])
    for i in range(13,len(input)):
        if len(set(input[i-13:i+1])) == 14:
            print(i+1)
            break


if __name__ == '__main__':
    part1()
    part2()