"""
Template from
https://realpython.com/python-advent-of-code/
"""
import pathlib
import sys

def elf_food(data):
    elf = list()
    food = list()
    for line in data:
        line = line.strip()
        if len(line)==0:
            elf.append(sum(food))
            food = list()
        else:
            food.append(int(line))
    return elf

def parse(puzzle_input):
    """Parse input."""
    return [line for line in puzzle_input.split("\n")]

def part1(data):
    """Solve part 1."""
    return max(elf_food(data))

def part2(data):
    """Solve part 2."""
    return sum(sorted(elf_food(data),reverse=True)[0:3])

def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))