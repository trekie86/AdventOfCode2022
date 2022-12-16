from utils.fileutil import read_file_to_string_list
from typing import Tuple, List
import sys

AIR = "."
ROCK = "#"
SAND_SOURCE = "+"
SAND = "o"


def part1():
    input = read_file_to_string_list("adventofcode/day14/input.txt")
    min_width, max_width, max_height = get_min_max_values(input)
    model = build_model(input, min_width, max_width, max_height)
    # print_model(model)
    count = 0
    while not trickle_sand(model, min_width):
        count += 1
        # print_model(model)
    print(count)


def part2():
    input = read_file_to_string_list("adventofcode/day14/input.txt")
    min_width, max_width, max_height = get_min_max_values(input)
    max_height += 2
    model = build_model_part_2(input, max_width, max_height)
    # print_model(model)
    count = 0
    full = False
    while not full:
        full = (
            model[1][500] == SAND
            and model[1][500 + 1] == SAND
            and model[1][500 - 1] == SAND
        )
        trickle_sand(model, min_width, True)
        # print_model(model)
        count += 1
    print(count)


def get_min_max_values(input: str) -> Tuple[int, int, int]:
    max_width = 0
    max_height = 0
    min_width = sys.maxsize
    for line in input:
        pairs = line.split(" -> ")
        for pair in pairs:
            width, height = map(int, pair.split(","))
            if width > max_width:
                max_width = width
            if width < min_width:
                min_width = width
            if height > max_height:
                max_height = height
    return min_width, max_width, max_height


def build_model(
    input: str, min_width: int, max_width: int, max_height: int
) -> List[List[str]]:
    model = [
        [AIR for _ in range(min_width, max_width + 1)] for _ in range(max_height + 1)
    ]
    model[0][500 - min_width] = SAND_SOURCE

    for bounds in input:
        pairs = bounds.split(" -> ")
        for i in range(len(pairs) - 1):
            p1, p2 = map(int, pairs[i].split(","))
            p3, p4 = map(int, pairs[i + 1].split(","))
            if p2 == p4:
                y = p2
                for x in range(min(p1, p3) - min_width, max(p1, p3) - min_width + 1):
                    model[y][x] = ROCK
            else:
                x = p1 - min_width
                for y in range(min(p2, p4), max(p2, p4)):
                    model[y][x] = ROCK
    return model


def build_model_part_2(input: str, max_width: int, max_height: int) -> List[List[str]]:
    model = [[AIR for _ in range(max_width + 1)] for _ in range(max_height + 1)]
    model[0][500] = SAND_SOURCE
    for i in range(len(model[0])):
        model[max_height][i] = ROCK

    for bounds in input:
        pairs = bounds.split(" -> ")
        for i in range(len(pairs) - 1):
            p1, p2 = map(int, pairs[i].split(","))
            p3, p4 = map(int, pairs[i + 1].split(","))
            if p2 == p4:
                y = p2
                for x in range(min(p1, p3), max(p1, p3) + 1):
                    model[y][x] = ROCK
            else:
                x = p1
                for y in range(min(p2, p4), max(p2, p4)):
                    model[y][x] = ROCK
    return model


def grow_width(model: List[List[str]]) -> None:
    for i in range(len(model)):
        model[i].append(AIR)
    model[len(model)-1][len(model[0])-1] = ROCK


def print_model(model: List[List[str]]):
    for row in model:
        print("".join(row))


def trickle_sand(model: List[List[str]], min_width: int, grow: bool = False) -> bool:
    sand_pos_y = 0
    sand_pos_x = (500 - min_width) if not grow else 500
    blocked = False
    while not blocked:
        if sand_pos_x == len(model[0]) - 1:
            grow_width(model)
        if (
            (sand_pos_y + 1 >= len(model)
            or sand_pos_x - 1 < 0
            or sand_pos_x + 1 >= len(model[0]))
            and not grow
        ):
            # This means it's going to fall off the bottom of the model
            return True
        next_pos = model[sand_pos_y + 1][sand_pos_x]
        if next_pos == AIR:
            sand_pos_y += 1
        elif next_pos == ROCK or next_pos == SAND:
            if sand_pos_x - 1 >= 0 and model[sand_pos_y + 1][sand_pos_x - 1] == AIR:
                sand_pos_x -= 1
                sand_pos_y += 1
            elif (
                sand_pos_x + 1 <= len(model[0])
                and model[sand_pos_y + 1][sand_pos_x + 1] == AIR
            ):
                sand_pos_x += 1
                sand_pos_y += 1
            else:
                model[sand_pos_y][sand_pos_x] = SAND
                blocked = True
    return False


if __name__ == "__main__":
    part1()
    part2()
