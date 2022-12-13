from queue import Queue


def part1():
    map = read_file_to_2d_grid("adventofcode/day12/input.txt")
    start_x, start_y = find_starting_coordinates(map)
    # distance, path = find_path(map, start_x, start_y)
    # print(f"Distance: {distance}, path: {path}")
    distance = find_path(map, start_x, start_y)
    print(f"Distance: {distance}")


def part2():
    map = read_file_to_2d_grid("adventofcode/day12/input.txt")
    starting_points = find_all_starting_coordinates(map)
    path_lengths = []
    for start_x, start_y in starting_points:
        result = find_path(map, start_x, start_y)
        if result is not None:
            path_lengths.append(result)
    print(min(path_lengths))


def read_file_to_2d_grid(filename):
    with open(filename, "r") as f:
        grid = []
        for line in f:
            grid.append(list(line.strip()))
    return grid


def find_starting_coordinates(grid):
    for y, row in enumerate(grid):
        for x, col in enumerate(row):
            if col == "S":
                return x, y


def find_all_starting_coordinates(grid):
    start_coordinates = []
    for y, row in enumerate(grid):
        for x, col in enumerate(row):
            if col == "a" or col == "S":
                start_coordinates.append((x, y))
    return start_coordinates


def find_path(grid, start_x, start_y):
    q = Queue()
    visited = set([])
    q.put((start_x, start_y, 0))
    while not q.empty():
        # x, y, distance, curr_path = q.get_nowait()
        x, y, distance = q.get_nowait()
        if (x, y) in visited:
            continue
        # new_path = curr_path + f" -> ({x},{y})"
        visited.add((x, y))
        # print(f"({x},{y})")
        # print(distance)
        q_val = grid[y][x]
        if q_val == "E":
            # return distance, new_path
            return distance
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_x = x + dx
            new_y = y + dy
            if (
                ((new_x, new_y) not in visited)
                and 0 <= new_x < len(grid[0])
                and 0 <= new_y < len(grid)
            ):
                new_val = grid[new_y][new_x]
                if ord_val(new_val) - ord_val(q_val) <= 1:
                    # q.put((new_x, new_y, distance + 1, new_path))
                    q.put((new_x, new_y, distance + 1))


def ord_val(char):
    if char == "S":
        return 0
    elif char == "E":
        return 25
    else:
        return ord(char) - ord("a")


if __name__ == "__main__":
    part1()
    part2()
