from utils.fileutil import read_file_to_string_list

def part1():
    rucksacks: list[str] = read_file_to_string_list('adventofcode/day3/input.txt')
    total = 0
    for sack in rucksacks:
        first_half = set(sack[:len(sack)//2])
        second_half = set(sack[len(sack)//2:])
        overlap = next(iter((first_half & second_half)))
        # print(overlap)
        total += get_priority(overlap)
    print(total)

def part2():
    rucksacks: list[str] = read_file_to_string_list('adventofcode/day3/input.txt')
    total = 0
    for i in range(0, len(rucksacks), 3):
        a = set(rucksacks[i])
        b = set(rucksacks[i+1])
        c = set(rucksacks[i+2])
        common = next(iter(a & b & c))
        total += get_priority(common)
    print(total)


def get_priority(letter: str) -> int:
    if letter >= 'a':
        return ord(letter) - ord('a') + 1
    else:
        return ord(letter) - ord('A') + 27

if __name__ == '__main__':
    part1()
    part2()

