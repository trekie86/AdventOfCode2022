from utils.fileutil import read_file_to_string_list

def part1():
    input = read_file_to_string_list("adventofcode/day8/input.txt")
    grid = build_2d_grid_of_ints(input)
    circumference = 2 * len(grid) + 2 * len(grid[0]) - 4
    result = find_visible_trees(grid)
    print(len(result) + circumference)


def part2():
    input = read_file_to_string_list("adventofcode/day8/input.txt")
    grid = build_2d_grid_of_ints(input)
    print(find_max_viewing_distance(grid))


def build_2d_grid_of_ints(input):
    grid = []
    for line in input:
        grid.append(list(map(int, list(line))))
    return grid


def find_visible_trees(grid: list[list[int]]) -> set[tuple]:
    visible = set([])

    # traverse from left
    for i in range(1, len(grid) - 1):
        max_in_row = grid[i][0]
        for j in range(1, len(grid[0]) - 1):
            current = grid[i][j]
            if grid[i][j] > max_in_row:
                visible.add((i, j))
                max_in_row = grid[i][j]

    # count from right
    for i in range(1, len(grid) - 1):
        max_in_row = grid[i][len(grid[0]) - 1]
        for j in range(len(grid[0]) - 2, 0, -1):
            current = grid[i][j]
            if grid[i][j] > max_in_row:
                visible.add((i, j))
                max_in_row = grid[i][j]

    # count from top
    for i in range(1, len(grid) - 1):
        max_in_column = grid[0][i]
        for j in range(1, len(grid[0]) - 1):
            current = grid[j][i]
            if grid[j][i] > max_in_column:
                visible.add((j, i))
                max_in_column = grid[j][i]

    # count from bottom
    for i in range(1, len(grid) - 1):
        max_in_column = grid[len(grid[0]) - 1][i]
        for j in range(len(grid[0]) - 2, 0, -1):
            current = grid[j][i]
            if grid[j][i] > max_in_column:
                visible.add((j, i))
                max_in_column = grid[j][i]
    return visible


def find_max_viewing_distance(grid) -> int:
    max_vis = 0
    for pos_i in range(1, len(grid) - 1):
        for pos_j in range(1, len(grid[0]) - 1):
            current = grid[pos_i][pos_j]
            count_1, count_2, count_3, count_4 = 0, 0, 0, 0
            for i in range(pos_i-1, -1, -1):
                if grid[i][pos_j] < current:
                    count_1 += 1
                else:
                    count_1 += 1
                    break
            for i in range(pos_i+1, len(grid)):
                if grid[i][pos_j] < current:
                    count_2 += 1
                else:
                    count_2 += 1
                    break
            for j in range(pos_j-1, -1, -1):
                if grid[pos_i][j] < current:
                    count_3 += 1
                else:
                    count_3 += 1
                    break
            for j in range(pos_j+1, len(grid[0])):
                if grid[pos_i][j] < current:
                    count_4 += 1
                else:
                    count_4 += 1
                    break
            max_vis = max(max_vis, count_1*count_2*count_3*count_4)

    return max_vis


if __name__ == "__main__":
    part1()
    part2()
