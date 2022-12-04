from utils.fileutil import read_file_to_string_list

def part1():
    assignments = read_file_to_string_list('adventofcode/day4/input.txt')
    overlap = 0
    for assignment in assignments:
        first_pair, second_pair = assignment.split(',')
        first_start, first_end = map(int, first_pair.split('-'))
        second_start, second_end = map(int, second_pair.split('-'))

        if first_start <= second_start and first_end >= second_end:
            overlap += 1
        elif second_start <= first_start and second_end >= first_end:
            overlap += 1

    print(overlap)

def part2():
    assignments = read_file_to_string_list('adventofcode/day4/input.txt')
    overlap = 0
    for assignment in assignments:
        first_pair, second_pair = assignment.split(',')
        first_start, first_end = map(int, first_pair.split('-'))
        second_start, second_end = map(int, second_pair.split('-'))

        if first_start <= second_start and first_end >= second_end:
            overlap += 1
        elif second_start <= first_start and second_end >= first_end:
            overlap += 1
        elif first_end >= second_start and first_start <= second_start:
            overlap += 1
        elif second_end >= first_start and second_start <= first_start:
            overlap += 1

    print(overlap)

if __name__ == '__main__':
    part1()
    part2()