"""
Template from
https://realpython.com/python-advent-of-code/
"""
import pathlib
import sys

# Python program to illustrate the intersection
# of two lists using set() method
def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

def parse(puzzle_input):
    """Parse input."""
    return [line for line in puzzle_input.split("\n")]

def part1(data):
    """Solve part 1."""
    compartments = []
    for line in data:
        itme_cnt = len(line)
        common = list(set(line[0:int(itme_cnt/2)]) & set(line[int(itme_cnt/2):]))
        common = ord(common[0]) - 96 if ord(common[0])> 96 else ord(common[0])-65+27
        compartments.append(common)

    #print(compartments, sum(compartments))
    return sum(compartments)

def part2(data):
    """Solve part 2."""
    compartments = []
    group = 0
    while group < len(data)-2:
        common = list(set(data[group]) & set(data[group+1]) & set(data[group+2]))
        common = ord(common[0]) - 96 if ord(common[0])> 96 else ord(common[0])-65+27
        compartments.append(common)
        group = group + 3
    #print(compartments, sum(compartments))
    return sum(compartments)


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