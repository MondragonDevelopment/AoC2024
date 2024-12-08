def isSafe(rep):
    order = rep[0] - rep[-1]
    if order == 0: return False
    elif order > 0:
        i = 1
        while i < len(rep):
            if rep[i-1] < rep[i]: return False
            diff = abs(rep[i-1] - rep[i])
            if diff > 3 or diff == 0: return False
            i += 1
    else:
        i = 1
        while i < len(rep):
            if rep[i-1] > rep[i]: return False
            diff = abs(rep[i-1] - rep[i])
            if diff > 3 or diff == 0: return False
            i += 1
    return True


with open("data/day2.txt") as data:
    lines = data.read().strip().split("\n")

reports = [[int(c) for c in line.split()] for line in lines]
#print(reports)
safe = 0

for report in reports:
    if isSafe(report): safe += 1
    else:
        #print(report)
        for i in range(len(report)):
            #print(report[:i] + report[i+1:])
            if isSafe(report[:i] + report[i+1:]): 
                safe += 1
                break

print(safe)


def isSafe2(report, flag = False):
    rep = [i for i in report]
    order = rep[0] - rep[1]
    fake = 0

    while fake < 2:
        i = 1
        if order == 0:
            fake += 1
            rep.pop(i-1)
            print(i)
            continue
        elif order > 0:
            while i < len(rep):
                diff = abs(rep[i-1] - rep[i])
                if rep[i-1] < rep[i] or diff > 3 or diff == 0: 
                    fake += 1
                    rep.pop(i-1)
                    print(i)
                    continue
                i += 1
        else:
            while i < len(rep):
                diff = abs(rep[i-1] - rep[i])
                if rep[i-1] > rep[i] or diff > 3 or diff == 0:
                    fake += 1
                    rep.pop(i-1)
                    print(i)
                    continue
                i += 1
        return True
    else :
        head = False
        if not flag:
            head = isSafe2(report[1:], True)
        if not head: return False
        elif head: return False
    return True

"""
safe = 0

for report in reports:
    print(report)
    if isSafe2(report): safe += 1

print(safe)
"""