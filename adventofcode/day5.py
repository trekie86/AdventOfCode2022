from queue import LifoQueue
import re

from utils.fileutil import read_file_to_string_list
from utils.list_util import split_lists_by_whitespace

class Instruction:
    """
    An instruction class for tracking what operations to take.
    """
    def __init__(self, quantity: int, fromPos: int, toPos: int) -> None:
        self.qty = quantity
        self.fromPos = fromPos
        self.toPos = toPos

def part1():
    raw = read_file_to_string_list("adventofcode/day5/input.txt")
    config, raw_instructions = split_lists_by_whitespace(raw)
    quequeMap: dict[int, LifoQueue[str]] = parseCrates(config)

    for input in raw_instructions:
        processInstructions(quequeMap, parseInstruction(input))
    getTopCrates(quequeMap)

def part2():
    raw = read_file_to_string_list("adventofcode/day5/input.txt")
    config, raw_instructions = split_lists_by_whitespace(raw)
    quequeMap: dict[int, LifoQueue[str]] = parseCrates(config)

    for input in raw_instructions:
        processInstructionsV2(quequeMap, parseInstruction(input))
    getTopCrates(quequeMap)

def parseCrates(input: list[str]) -> dict[int, LifoQueue[str]]:
    """
    This function reads the string list input and builds the map & stack object.

    Args:
        input (list[str]): The values that visualize the container configuration at start.

    Returns:
        dict[int, LifoQueue[str]]: A logical representation of the containers,
        a map that is keyed by the container id and a stack that is the boxes within the container.
    """
    quequeMap: dict[int, LifoQueue[str]] = {}

    buckets = re.finditer('\d', input[-1])
    for bucket in buckets:
        idx = bucket.span()[0]
        pos = int(bucket.group())
        new_stack: LifoQueue[str] = LifoQueue()
        for row in input[-2::-1]:
            if len(row) > idx and row[idx].strip() != '':
                new_stack.put(row[idx])
        quequeMap[pos] = new_stack
    return quequeMap

def parseInstruction(input: str) -> Instruction:
    """
    Takes the string value from the input file and converts it into an instruction class. Boxes are moved in a LIFO manner.
    """
    parts = input.split(' ')
    return Instruction(int(parts[1]), int(parts[3]), int(parts[5]))

def processInstructions(quequeMap: dict[int, LifoQueue[str]], instruction: Instruction) -> None:
    """
    Process the instructions and manipulate the contents of the queueMap.
    Args:
        quequeMap (dict[int, LifoQueue[str]]): The containers and packages to be manipulated.
        instruction (Instruction): The instruction to execute.
    """
    for _ in range(instruction.qty):
        temp: str = quequeMap[instruction.fromPos].get_nowait()
        quequeMap[instruction.toPos].put(temp)

def processInstructionsV2(quequeMap: dict[int, LifoQueue[str]], instruction: Instruction) -> None:
    """
    Process the instructions and manipulate the contents of the queueMap. In this variation, the items are "moved" multiple at a time.
    Args:
        quequeMap (dict[int, LifoQueue[str]]): The containers and packages to be manipulated.
        instruction (Instruction): The instruction to execute.
    """
    # I'm sure there is a more efficient way to do this but the set of data is not large, it's okay
    tempLifo = LifoQueue()
    for _ in range(instruction.qty):
        tempLifo.put(quequeMap[instruction.fromPos].get_nowait())
    while not tempLifo.empty():
        quequeMap[instruction.toPos].put(tempLifo.get_nowait())


def getTopCrates(quequeMap: dict[int, LifoQueue[str]]) -> None:
    """
    Scan through the queueMap and extrack the "top" package from each container.
    Print out the results.

    Args:
        quequeMap (dict[int, LifoQueue[str]]): The container and boxes to scan
    """
    result = ''
    for k in sorted(quequeMap.keys()):
        result += quequeMap[k].get()
    print(result)

if __name__ == "__main__":
    part1()
    part2()


