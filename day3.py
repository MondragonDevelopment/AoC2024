with open("data/day3.txt") as data:
    lines = data.read().strip().split("\n")

def getLocations(string, substring):
    locations = []
    startIdx = 0
    while startIdx < (len(string) - len(substring) + 1):
        nextIdx = string.find(substring, startIdx)
        if nextIdx != -1:
            locations.append([nextIdx + 4, string.find(")", nextIdx + 4), ])
            startIdx = nextIdx + 1
        else:
            break
    return locations

def spotNums(string):
    nums = [i for i in string.split(",")]
    try:
        return int(nums[0]) * int(nums[1])
    except: return 0

def part2(string):
    substring = "mul("
    locations = []
    startIdx, prevIns= 0, 0
    while prevIns < (len(string) - len(substring) + 1):
        nextdont = string.find("don't()", prevIns + 4)
        nextMul = string.find(substring, startIdx)
        print(prevIns, nextMul, nextdont)
        if nextMul == -1: break
        elif nextMul > nextdont and nextdont != -1:
            nextdo = string.find("do()", nextdont + 1)
            if nextdo == -1: break
            prevIns = nextdo
            startIdx = prevIns
            print(prevIns, nextMul, nextdont)
            continue
        else:
            print("appending", nextMul)
            locations.append([nextMul + 4, string.find(")", nextMul + 4), ])
            startIdx = nextMul + 1
    return locations


sum = 0
fullprogram = "".join(lines)
print(len(fullprogram))

locs = part2(fullprogram)
for loc in locs:
    sum += spotNums(fullprogram[loc[0]:loc[1]])

print(sum)

"""
for line in lines:
    #locs = getLocations(line, "mul(")
    locs2 = part2(line)
    print(locs2)
    for loc in locs2:
        sum += spotNums(line[loc[0]:loc[1]]) 

print(sum)
"""
