import ast
from utils.fileutil import read_file_to_string_list
from utils.list_util import split_lists_by_whitespace
import math
from functools import cmp_to_key


def part1():
    raw_input = read_file_to_string_list("adventofcode/day13/input.txt")
    packet_pairs = split_lists_by_whitespace(raw_input)

    valid_pairs = []
    for idx, pairs in enumerate(packet_pairs):
        packet_1 = ast.literal_eval(pairs[0])
        packet_2 = ast.literal_eval(pairs[1])
        if validate_packets(packet_1, packet_2):
            valid_pairs.append(idx + 1)
    print(sum(valid_pairs))


def part2():
    raw_input = read_file_to_string_list("adventofcode/day13/input.txt")
    raw_input.append('[[6]]')
    raw_input.append('[[2]]')
    cleaned_input = [x for x in raw_input if (x != "")]
    cleaned_input.sort(key=cmp_to_key(lambda a, b: result_to_compare(validate_packets(ast.literal_eval(a),ast.literal_eval(b)))))
    results = []
    for idx, vals in enumerate(cleaned_input):
        if vals == '[[6]]' or vals == '[[2]]':
            results.append(idx+1)
    print(math.prod(results))

def result_to_compare(val:bool|None):
    if val is None:
        return 0
    elif val:
        return -1
    else:
        return 1


def validate_packets(p1, p2) -> bool|None:
    idx = 0
    while idx < len(p1) and idx < len(p2):
        if type(p1[idx]) is int and type(p2[idx]) is int:
            if p1[idx] == p2[idx]:
                idx += 1
            else:
                return p1[idx] < p2[idx]
        elif type(p1[idx]) is list and type(p2[idx]) is list:
            result = validate_packets(p1[idx], p2[idx])
            if result is not None:
                return result
            else:
                idx += 1
        else:
            # Types are not the same, make the non-list a list
            if type(p1[idx]) is int:
                result = validate_packets([p1[idx]], p2[idx])
                if result is not None:
                    return result
                else:
                    idx += 1
            else:
                result = validate_packets(p1[idx], [p2[idx]])
                if result is not None:
                    return result
                else:
                    idx += 1
    if len(p1) == len(p2):
        return None
    if idx == len(p1):
        return True
    else:
        return False


if __name__ == "__main__":
    part1()
    part2()
