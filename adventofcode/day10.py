from utils.fileutil import read_file_to_string_list


def part1():
    input = read_file_to_string_list("adventofcode/day10/input.txt")
    register = build_register(input)
    # print(
    #     f"20: {register[20]}, 60: {register[60]}, 100: {register[100]}, 140: {register[140]}, 180: {register[180]}, 220: {register[220]}"
    # )
    print(
        register[20] * 20
        + register[60] * 60
        + register[100] * 100
        + register[140] * 140
        + register[180] * 180
        + register[220] * 220
    )


def part2():
    input = read_file_to_string_list("adventofcode/day10/input.txt")
    register = build_register(input)
    crt = []
    BRIGHT = "#"
    DARK = "."
    for i in range(0, 241):
        sprite = register[i+1]
        compare_val = i%40
        if compare_val >= sprite - 1 and compare_val <= sprite + 1:
            crt.append(BRIGHT)
        else:
            crt.append(DARK)

    print("".join(crt[1:40]))
    print("".join(crt[41:80]))
    print("".join(crt[81:120]))
    print("".join(crt[121:160]))
    print("".join(crt[161:200]))
    print("".join(crt[201:240]))



def build_register(input):
    register = []
    x = 1
    register.append(x)
    register.append(x)
    for instruction in input:
        if instruction == "noop":
            register.append(x)
        else:
            val = int(instruction.split(" ")[1])
            register.append(x)
            x += val
            register.append(x)
    return register


if __name__ == "__main__":
    part1()
    part2()
