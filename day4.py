from collections import defaultdict

with open("data/day4.txt") as data:
    lines = data.read().strip().split("\n")

grid = []

for line in lines:
    hor = [i for i in line]
    grid.append(hor)

def groups(data, func):
    grouping = defaultdict(list)
    for y in range(len(data)):
        for x in range(len(data[y])):
            grouping[func(x, y)].append(data[y][x])
    return list(map(grouping.get, sorted(grouping)))

def searchWord(string):
    startIdx = 0
    count = 0
    while True:
        nextF = string.find("XMAS", startIdx)
        nextB = string.find("SAMX", startIdx)
        if nextB != -1 and nextF != -1:
            next = min(nextF, nextB)
        elif nextB == -1:
            next = nextF
        elif nextF == -1:
            next = nextB
        else: next = -1
        if next != -1:
            count += 1
            startIdx = next + 3
        else: break
    return count

def counting(lista):
    parSum = 0
    for l in lista:
        string = "".join(l)
        x = searchWord(string)
        #print(string, x)
        parSum += x
    #print(parSum)
    return parSum

def check(c1, c2):
    if (c1 == "M" and c2 == "S") or (c1 == "S" and c2 == "M"): return True
    else: return False


def part2(matrix):
    count = 0
    #print(len(matrix) - 2)
    for row in range(1, len(matrix) - 1):
        for col in range(1, len(matrix) - 1):
            if matrix[row][col] == "A":
                # surr = [line[col - 1 : col + 2] for line in matrix[row - 1 : row +2]]
                if check(matrix[row + 1][col - 1], matrix[row - 1][col + 1]) and check(matrix[row + 1][col + 1], matrix[row - 1][col - 1]):
                    count += 1
    return count

"""
cols = groups(grid, lambda x, y: x)
rows = groups(grid, lambda x, y: y)
fdiag = groups(grid, lambda x, y: x + y)
bdiag = groups(grid, lambda x, y: x - y)

result = 0


paths = [cols, rows, bdiag, fdiag]

for path in paths:
    result += counting(path)

print(result)
"""

print(part2(grid))
