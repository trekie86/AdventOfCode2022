from utils.fileutil import read_file_to_string_list


def part1():
    instructions = read_file_to_string_list("adventofcode/day9/input.txt")
    H, T, = (0,0), (0, 0)
    covered = set([])
    covered.add(T)
    for instruction in instructions:
        direction, qty = instruction.split(" ")
        qty = int(qty)
        for _ in range(qty):
            match direction:
                case "R":
                    H = (H[0] + 1, H[1])
                case "L":
                    H = (H[0] - 1, H[1])
                case "U":
                    H = (H[0], H[1] + 1)
                case "D":
                    H = (H[0], H[1] - 1)
            distance = distance_between_knots(H, T)
            if distance >= 2 and not is_diag(H, T):
                # do something
                match direction:
                    case "R":
                        T = (T[0] + 1, T[1])
                    case "L":
                        T = (T[0] - 1, T[1])
                    case "U":
                        T = (T[0], T[1] + 1)
                    case "D":
                        T = (T[0], T[1] - 1)
            elif distance > 2 and is_diag(H, T):
                # do something else
                match direction:
                    case "R":
                        T = (H[0] - 1, H[1])
                    case "L":
                        T = (H[0] + 1, H[1])
                    case "U":
                        T = (H[0], H[1] - 1)
                    case "D":
                        T = (H[0], H[1] + 1)
            covered.add(T)
    print(len(covered))


def part2():
    movement = {
        (-2, -2): (-1, -1),
        (-2, -1): (-1, -1),
        (-2, 0): (-1, 0),
        (-2, 1): (-1, 1),
        (-2, 2): (-1, 1),
        (2, -2): (1, -1),
        (2, -1): (1, -1),
        (2, 0): (1, 0),
        (2, 1): (1, 1),
        (2, 2): (1, 1),
        (-1, 2): (-1, 1),
        (0, 2): (0, 1),
        (1, 2): (1, 1),
        (-1, -2): (-1, -1),
        (0, -2): (0, -1),
        (1, -2): (1, -1),
    }
    instructions = read_file_to_string_list("adventofcode/day9/input.txt")
    knots: list[tuple[int, int]] = [(0, 0)] * 10
    covered = set([])
    covered.add(knots[-1])
    for instruction in instructions:
        direction, qty = instruction.split(" ")
        qty = int(qty)
        for _ in range(qty):
            match direction:
                case "R":
                    knots[0] = (knots[0][0] + 1, knots[0][1])
                case "L":
                    knots[0] = (knots[0][0] - 1, knots[0][1])
                case "U":
                    knots[0] = (knots[0][0], knots[0][1] + 1)
                case "D":
                    knots[0] = (knots[0][0], knots[0][1] - 1)

            for i in range(len(knots) - 1):
                dx = knots[i][0] - knots[i + 1][0]
                dy = knots[i][1] - knots[i + 1][1]
                if (dx, dy) in movement:
                    knots[i + 1] = (
                        knots[i + 1][0] + movement[(dx, dy)][0],
                        knots[i + 1][1] + movement[(dx, dy)][1],
                    )
            covered.add(knots[-1])

    print(len(covered))


def distance_between_knots(h: tuple[int, int], t: tuple[int, int]):
    return abs(h[0] - t[0]) + abs(h[1] - t[1])


def is_diag(h: tuple[int, int], t: tuple[int, int]):
    return h[0] != t[0] and h[1] != t[1]


if __name__ == "__main__":
    part1()
    part2()
