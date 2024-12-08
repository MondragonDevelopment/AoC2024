def topSort(G):
    S, res = set(), []
    def recurse(u):
        if u in S: return 
        S.add(u)
        for v in G[u]:
            try: recurse(v)
            except: 
                S.add(v)
                res.append(v)
        res.append(u)

    for u in G: recurse(u)
    res.reverse()
    return res

"""
def checkOrder(upd):
    curr = -1
    for entry in upd:
        if entry not in pairs: continue
        elif pairs[entry] < curr: 
            print(update, curr, entry)
            return False
        else: curr = max(pairs[entry], curr)
    return True
"""

def checkOrder2(upd):
    for i in range(1, len(upd)):
        if upd[i] not in G[upd[i-1]]: return False
    return True

with open("data/day5.txt") as data:
    rules, updates = data.read().split("\n\n")

G = {}

for line in rules.split("\n"):
    key, val = map(int, line.split("|"))
    if key not in G:
        G[key] = [val]
    else:
        G[key].append(val)

for k in G:
    print(k, G[k])

#order = topSort(G)
#ord2 = [x.split(',') for x in updates.split('\n')]
#pairs = {}
res = 0
res2 = 0

#for i in range(len(order)):
    #pairs[order[i]] = i

#print(order)
#print(ord2)
#print(pairs)

for update in updates.split("\n"):
    entry = [int(x) for x in update.split(",")]
    #print(entry, checkOrder(entry))
    inOrder = checkOrder2(entry)
    if inOrder: 
        res += entry[len(entry)//2]
    else:
        entry = sorted(entry, key=lambda x: -sum(f"{x}|{y}" in rules for y in entry))   # I don't know why you have to sum them. Taken from https://topaz.github.io/paste/#XQAAAQB0AQAAAAAAAAA5HUm7ztOXp6VRzN9HFLOXu+qLvAXXnjtDkvLBkVojYocD1X0L+WJA4fopjSVxw7xeOe48vDeDFt0UTVhsUr9cR6472tXLOd4rzT6JVCJprVLhtTgvzpa24Lgbo3IVZ2xM0UVJQYCnvj7hDGgex2bgu1pLksjJF+p/TeZc5rH6j6p7/8cEkoeE6m2sS8/79ZH4A/hxEfdg6OcQeA7UZeB669n2I7A0EJQXPrY525lykKD34BZ6QEGoqrze7ZJFXPb/D8qpAA==
        res2 += entry[len(entry)//2]




print(res, res2)
