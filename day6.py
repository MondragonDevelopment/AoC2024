G = {i+j*1j: char for i,row in enumerate(open('data/day6.txt'))
               for j,char in enumerate(row.strip())}

print(G)

start = min(p for p in G if G[p] == '^')
print(start)

def walk(G):
    pos, dir, seen = start, -1, set()
    while pos in G and (pos,dir) not in seen:
        seen |= {(pos,dir)}
        if G.get(pos+dir) == "#":
            dir *= -1j
        else: pos += dir
    return {p for p,_ in seen}, (pos,dir) in seen

path = walk(G)[0]
print(walk(G))

print(len(path), 
      sum(walk(G | {o: '#'})[1] for o in path if o != start))
