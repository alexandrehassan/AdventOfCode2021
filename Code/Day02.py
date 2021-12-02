from Common import get_lines, time_function


def part1() -> int:
    posX, posY = 0, 0
    for line in lines:
        instruction = line.split(" ")[0]
        distance = int(line.split(" ")[1])
        if instruction == "up":
            posY -= distance
        elif instruction == "down":
            posY += distance
        elif instruction == "forward":
            posX += distance
        else:
            print("Something went wrong")
    return posX * posY


def part2() -> int:
    posX, posY, aim = 0, 0, 0
    for line in lines:
        instruction = line.split(" ")[0]
        distance = int(line.split(" ")[1])
        if instruction == "up":
            aim -= distance
        elif instruction == "down":
            aim += distance
        elif instruction == "forward":
            posX += distance
            posY += aim * distance
        else:
            print("Something went wrong")
    return posX * posY


if __name__ == "__main__":
    lines = get_lines("Inputs/Day02.txt")

    # Part 1: 1989265
    print(f"Part 1: {part1()}")
    # Part 2: 2089174012
    print(f"Part 2: {part2()}")

    # Part 1: 0.0007306340010836721s
    print(f"Part 1: {time_function(part1)}s")
    # Part 2: 0.0008213049988262355s
    print(f"Part 2: {time_function(part2)}s")
