from utils.fileutil import read_file_to_string_list
from utils.list_util import split_lists_by_whitespace

def part1():
    """
    Get the most calories an elf has.
    """
    calories = read_file_and_get_calories()
    max_cal = max(calories)
    print(max_cal)

def part2():
    """
    Get the sum of the top 3 elves calories.
    """
    calories = read_file_and_get_calories()
    total_cal = sum(calories[:3])
    print(total_cal)

def read_file_and_get_calories() -> list[int]:
    """
    Read the file and split it into a list of calories per elf.
    Returns:
        list[int]: The list of calories per elf sorted by largest to smallest
    """
    vals = read_file_to_string_list("adventofcode/day1/input.txt")
    calories = [map(int, i) for i in split_lists_by_whitespace(vals)]
    calories = sorted([sum(i) for i in calories], reverse=True)
    return calories

if __name__ == '__main__':
    part1()
    part2()


