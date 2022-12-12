from day11.monkey import Monkey, build_monkey
from utils.list_util import split_lists_by_whitespace
from utils.fileutil import read_file_to_string_list
import math
from queue import Queue
from typing import Callable


def part1():
    play_monkey_games(20, 3)


def part2():
    play_monkey_games(10_000)

def play_monkey_games(rounds: int, worry_reducer: int = 1):
    raw_input = read_file_to_string_list("adventofcode/day11/input.txt")
    raw_monkeys = split_lists_by_whitespace(raw_input)
    monkey_map = {}
    for raw_monkey in raw_monkeys:
        monkey = build_monkey(raw_monkey)
        monkey_map[monkey.id] = monkey
    lcm = math.lcm(*[x.divisor for x in monkey_map.values()])
    for _ in range(rounds):
        for i in range(0, len(monkey_map)):
            monkey = monkey_map[i]
            while not monkey.items.empty():
                item = monkey.items.get_nowait()
                new_val = monkey.operate(item) // worry_reducer % lcm
                to = monkey.eval(new_val)
                monkey_map[to].items.put(new_val)
    print(get_monkey_business(monkey_map))


def get_monkey_business(monkey_map: dict[int, Monkey]) -> int:
    monkey_list = list(monkey_map.values())
    monkey_list.sort(key=lambda x: x.inspection_count, reverse=True)
    return math.prod([x.inspection_count for x in monkey_list[:2]])


if __name__ == "__main__":
    part1()
    part2()
