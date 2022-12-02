from utils.fileutil import read_file_to_string_list

from enum import Enum

def part1():
    moves = read_file_to_string_list('adventofcode/day2/input.txt')
    result = 0
    for move in moves:
        op, me = move.split(' ')
        code: ThrowValue = codeToThrow[me]
        result += code.value
        rule = rules[(codeToThrow[op], codeToThrow[me])]
        result += rule.value

    print(result)

def part2():
    moves = read_file_to_string_list('adventofcode/day2/input.txt')
    result = 0
    for move in moves:
        op, outcome = move.split(' ')
        result += keyToResult[outcome].value
        throw = newRules[(codeToThrow[op], keyToResult[outcome])]
        result += throw.value

    print(result)


class ThrowValue(Enum):
    ROCK = 1
    PAPER = 2
    SCISSSORS = 3

class GameOutcome(Enum):
    WIN = 6
    LOSE = 0
    DRAW = 3

codeToThrow = {
    'X': ThrowValue.ROCK,
    'Y': ThrowValue.PAPER,
    'Z': ThrowValue.SCISSSORS,
    'A': ThrowValue.ROCK,
    'B': ThrowValue.PAPER,
    'C': ThrowValue.SCISSSORS
}

rules = {
    (ThrowValue.ROCK, ThrowValue.PAPER): GameOutcome.WIN,
    (ThrowValue.ROCK, ThrowValue.SCISSSORS): GameOutcome.LOSE,
    (ThrowValue.ROCK, ThrowValue.ROCK): GameOutcome.DRAW,
    (ThrowValue.PAPER, ThrowValue.ROCK): GameOutcome.LOSE,
    (ThrowValue.PAPER, ThrowValue.PAPER): GameOutcome.DRAW,
    (ThrowValue.PAPER, ThrowValue.SCISSSORS): GameOutcome.WIN,
    (ThrowValue.SCISSSORS, ThrowValue.ROCK): GameOutcome.WIN,
    (ThrowValue.SCISSSORS, ThrowValue.PAPER): GameOutcome.LOSE,
    (ThrowValue.SCISSSORS, ThrowValue.SCISSSORS): GameOutcome.DRAW
}

keyToResult = {
    'X': GameOutcome.LOSE,
    'Y': GameOutcome.DRAW,
    'Z': GameOutcome.WIN
}

newRules = {
    (ThrowValue.ROCK, GameOutcome.WIN): ThrowValue.PAPER,
    (ThrowValue.ROCK, GameOutcome.DRAW): ThrowValue.ROCK,
    (ThrowValue.ROCK, GameOutcome.LOSE): ThrowValue.SCISSSORS,
    (ThrowValue.PAPER, GameOutcome.WIN): ThrowValue.SCISSSORS,
    (ThrowValue.PAPER, GameOutcome.DRAW): ThrowValue.PAPER,
    (ThrowValue.PAPER, GameOutcome.LOSE): ThrowValue.ROCK,
    (ThrowValue.SCISSSORS, GameOutcome.WIN): ThrowValue.ROCK,
    (ThrowValue.SCISSSORS, GameOutcome.DRAW): ThrowValue.SCISSSORS,
    (ThrowValue.SCISSSORS, GameOutcome.LOSE): ThrowValue.PAPER
}

if __name__ == '__main__':
    part1()
    part2()